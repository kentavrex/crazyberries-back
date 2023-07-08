from db.schemas.comment import CreateCommentSchema, OutputCommentSchema, UpdateCommentSchema, InputCommentSchema
from repositories.comment import CommentsRepository


class CommentsService:
    def __init__(self, repository: CommentsRepository):
        self.repository = repository

    async def get_by_product_card_id(self, product_card_id: int, limit: int, skip: int) -> list[OutputCommentSchema]:
        return self.repository.get_by_product_card_id(product_card_id, limit, skip)

    async def create(self, product_card_id: int, data: InputCommentSchema) -> OutputCommentSchema:
        return self.repository.create(
            CreateCommentSchema(product_card_id=product_card_id, **data.dict())
        )

    async def update(self, comment_id: int, data: UpdateCommentSchema) -> OutputCommentSchema:
        return self.repository.update(comment_id, data)

    async def delete(self, comment_id: int):
        return self.repository.delete(comment_id)
