from fastapi import APIRouter, Depends
from db.schemas.comment import OutputCommentSchema, UpdateCommentSchema, InputCommentSchema
from repositories.comment import CommentsRepository
from endpoints import get_comments_repository
from services.comment_service import CommentsService

router = APIRouter()


@router.get("/{product_card_id}/comments", response_model=list[OutputCommentSchema])
async def get_comments(
        product_card_id: int,
        comments_repository: CommentsRepository = Depends(get_comments_repository),
        limit: int = 100,
        skip: int = 0,
):
    return CommentsService(comments_repository).get_by_product_card_id(product_card_id, limit, skip)


@router.post("/{product_card_id}/comments", response_model=OutputCommentSchema)
async def create_comment(
        product_card_id: int,
        data: InputCommentSchema,
        comments_repository: CommentsRepository = Depends(get_comments_repository)
):
    return CommentsService(comments_repository).create(product_card_id, data)


@router.patch("/{product_card_id}/comments/{comment_id}", response_model=OutputCommentSchema)
async def update_comment(
        product_card_id: int,
        comment_id: int,
        data: UpdateCommentSchema,
        comments_repository: CommentsRepository = Depends(get_comments_repository)
):
    return CommentsService(comments_repository).update(comment_id, data)


@router.delete("/{product_card_id}/comments/{comment_id}", status_code=204)
async def delete_comment(
        product_card_id: int,
        comment_id: int,
        comments_repository: CommentsRepository = Depends(get_comments_repository)
):
    return CommentsService(comments_repository).delete(comment_id)

