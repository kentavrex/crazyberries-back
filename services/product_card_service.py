from fastapi.encoders import jsonable_encoder

from db import models
from db.schemas.product_card import InputProductCardSchema, OutputProductCardSchema, UpdateProductCardSchema
from repositories.product_card import ProductCardRepository


class ProductCardService:
    def __init__(self, repository: ProductCardRepository):
        self.repository = repository

    async def get_all(self, limit: int, skip: int) -> list[OutputProductCardSchema]:
        return self.repository.get_all(limit, skip)

    async def get_by_id(self, product_card_id: int) -> OutputProductCardSchema:
        return self.repository.get_by_id(product_card_id)

    async def create(
            self, author_id: int, data: InputProductCardSchema
    ) -> list[OutputProductCardSchema]:
        data = models.ProductCard(**data.dict())
        data.author_id = author_id

        return self.repository.create(jsonable_encoder(data))

    async def update(self, product_card_id: int, data: UpdateProductCardSchema) -> OutputProductCardSchema:
        data = models.ProductCard(**data.dict())
        data.author_id = product_card_id

        return self.repository.update(jsonable_encoder(data))

    async def delete(self, product_card_id: int):
        return self.repository.delete(product_card_id)
