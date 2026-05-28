from fastapi import status
from httpx import AsyncClient


async def test_health_check_success(client: AsyncClient):
    # When
    response = await client.get("/health")

    # Then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status": "online",
        "ambiente": "desenvolvimento",
        "database_status": "conectado"
    }
