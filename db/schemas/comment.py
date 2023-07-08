import pytz

from db.schemas import CustomBase
from pydantic import validator
from datetime import datetime


class BaseCommentSchema(CustomBase):
    timestamp: datetime
    text: str
    author_id: int


class OutputCommentSchema(BaseCommentSchema):
    id: int | None = None
    product_card_id: int


class InputCommentSchema(BaseCommentSchema):

    @validator('timestamp')
    def wrong_timestamp(cls, v):
        if v > datetime.utcnow().replace(tzinfo=pytz.UTC):
            raise ValueError("Should not be later than now")
        return v


class UpdateCommentSchema(CustomBase):
    text: str


class CreateCommentSchema(InputCommentSchema):
    product_card_id: int
