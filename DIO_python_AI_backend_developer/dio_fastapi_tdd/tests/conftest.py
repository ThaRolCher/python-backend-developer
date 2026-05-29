import pytest
import asyncio
import bson
import bson.codec_options
from bson.binary import UuidRepresentation
import mongomock.codec_options

# Patch no BSON.encode para garantir que o UUID seja sempre serializado com representação STANDARD.
# Isso evita o ValueError de UuidRepresentation.UNSPECIFIED no PyMongo v4 durante os testes com mongomock.
original_encode = bson.BSON.encode

@classmethod
def patched_encode(cls, document, check_keys=False, codec_options=None):
    from bson.codec_options import CodecOptions
    from bson.binary import UuidRepresentation
    if codec_options is None:
        codec_options = CodecOptions(uuid_representation=UuidRepresentation.STANDARD)
    else:
        codec_options = codec_options.with_options(uuid_representation=UuidRepresentation.STANDARD)
    return original_encode(document, check_keys, codec_options)

bson.BSON.encode = patched_encode

# Patch no mongomock para suportar comparação de Decimal128
import mongomock.filtering
original_bson_compare = mongomock.filtering.bson_compare

def patched_bson_compare(op, a, b, can_compare_types=True):
    from bson import Decimal128
    if isinstance(a, Decimal128):
        a = a.to_decimal()
    if isinstance(b, Decimal128):
        b = b.to_decimal()
    return original_bson_compare(op, a, b, can_compare_types)

mongomock.filtering.bson_compare = patched_bson_compare



from uuid import UUID
from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductUpdate
from store.usecases.product import product_usecase
from tests.factories import product_data, products_data
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def mock_mongo(monkeypatch):
    from mongomock_motor import AsyncMongoMockClient
    mock_client = AsyncMongoMockClient()
    monkeypatch.setattr(db_client, "client", mock_client)
    return mock_client


@pytest.fixture
def mongo_client(mock_mongo):
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    db = mongo_client.get_database("store")
    collection_names = await db.list_collection_names()
    for collection_name in collection_names:
        if collection_name.startswith("system"):
            continue

        await db[collection_name].delete_many({})


@pytest.fixture
async def client() -> AsyncClient:
    from store.main import app
    from httpx import ASGITransport

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    return UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def product_up(product_id):
    return ProductUpdate(**product_data(), id=product_id)


@pytest.fixture
async def product_inserted(product_in):
    return await product_usecase.create(body=product_in)


@pytest.fixture
def products_in():
    return [ProductIn(**product) for product in products_data()]


@pytest.fixture
async def products_inserted(products_in):
    return [await product_usecase.create(body=product_in) for product_in in products_in]
