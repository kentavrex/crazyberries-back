from db import models
from db.schemas.product_card import OutputProductCardSchema
from repositories import BaseRepository


class ProductCardRepository(BaseRepository):
    model = models.ProductCard
    schema = OutputProductCardSchema
