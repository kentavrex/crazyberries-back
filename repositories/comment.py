from db.models import Comment
from db.schemas.comment import OutputCommentSchema
from errors import NotFoundError
from repositories import BaseRepository


class CommentsRepository(BaseRepository):
    model = Comment
    schema = OutputCommentSchema

    async def get_by_product_card_id(self, product_card_id: int, limit: int, skip: int) -> list[OutputCommentSchema]:
        query = self.model.select().where(self.model.c.id == product_card_id).limit(limit).offset(skip)
        db_response = await self.database.fetch_all(query=query)
        if db_response is None:
            raise NotFoundError(f"'{self.model.__name__}' object not found")
        return [self.schema.from_orm(obj) for obj in db_response]
