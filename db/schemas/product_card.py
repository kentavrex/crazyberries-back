from db.helpers import ProductCardStatus, ProductCardCategory
from db.schemas import CustomBase


class BaseProductCardSchema(CustomBase):
    title: str
    status: ProductCardStatus
    price: int
    category: ProductCardCategory
    description: str
    status: ProductCardStatus


class UpdateProductCardSchema(CustomBase):
    title: str
    status: ProductCardStatus = ProductCardStatus.new
    price: int
    category: ProductCardCategory
    description: str = None
    status: ProductCardStatus


class OutputProductCardSchema(BaseProductCardSchema):
    id: int | None
    author_id: int


class InputProductCardSchema(BaseProductCardSchema):
    """Class for data that user gives"""

    pass
