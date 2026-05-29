from typing import List
from uuid import UUID

from decimal import Decimal
import pytest
from store.core.exceptions import NotFoundException, InsertionException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_up, product_inserted):
    product_up.price = "7.500"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


async def test_usecases_create_duplicate_should_raise_insertion_exception(product_in):
    await product_usecase.create(body=product_in)
    with pytest.raises(InsertionException) as err:
        await product_usecase.create(body=product_in)
    
    assert "Product already exists with name: Iphone 14 Pro Max" in err.value.message


async def test_usecases_update_should_raise_not_found(product_up):
    with pytest.raises(NotFoundException) as err:
        await product_usecase.update(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"), body=product_up)
    
    assert "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9" in err.value.message


async def test_usecases_update_should_modify_updated_at(product_up, product_inserted):
    import asyncio
    old_updated_at = product_inserted.updated_at
    product_up.price = "6.500"
    
    await asyncio.sleep(0.01)
    result = await product_usecase.update(id=product_inserted.id, body=product_up)
    
    assert result.updated_at > old_updated_at


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_by_price_range_should_return_correct_items():
    result = await product_usecase.query(price_min=Decimal("5000"), price_max=Decimal("8000"))
    
    assert isinstance(result, List)
    assert len(result) == 2
    names = [item.name for item in result]
    assert "Iphone 12 Pro Max" in names
    assert "Iphone 13 Pro Max" in names
