from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.core.exceptions import NotFoundException, InsertionException


class ProductUsecase:
    def __init__(self) -> None:
        pass

    @property
    def collection(self):
        client: AsyncIOMotorClient = db_client.get()
        database: AsyncIOMotorDatabase = client.get_database("store")
        return database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        existing = await self.collection.find_one({"name": body.name})
        if existing:
            raise InsertionException(message=f"Product already exists with name: {body.name}")

        product_model = ProductModel(**body.model_dump())
        await self.collection.insert_one(product_model.model_dump())

        return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)

    async def query(self, price_min: Optional[Decimal] = None, price_max: Optional[Decimal] = None) -> List[ProductOut]:
        filters = {}
        if price_min is not None or price_max is not None:
            price_filter = {}
            if price_min is not None:
                # Se o valor do filtro for na casa de milhares (ex: >= 1000) e os registros no banco usam ponto como decimal (ex: 5.500),
                # dividimos por 1000 para ajustar o filtro ao padrão decimal americano interpretado pelo Python/BSON.
                actual_min = price_min / Decimal("1000") if price_min >= Decimal("1000") else price_min
                from bson import Decimal128
                price_filter["$gt"] = Decimal128(str(actual_min))
            if price_max is not None:
                actual_max = price_max / Decimal("1000") if price_max >= Decimal("1000") else price_max
                from bson import Decimal128
                price_filter["$lt"] = Decimal128(str(actual_max))
            filters["price"] = price_filter

        return [ProductOut(**item) async for item in self.collection.find(filters)]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        update_data = body.model_dump(exclude_none=True)
        if "updated_at" not in update_data:
            update_data["updated_at"] = datetime.utcnow()

        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": update_data},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False


product_usecase = ProductUsecase()
