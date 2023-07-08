from fastapi import APIRouter, Depends

from db.schemas.product_card import InputProductCardSchema, UpdateProductCardSchema, OutputProductCardSchema
from endpoints import get_product_card_repository
from services.product_card_service import ProductCardService
from repositories.product_card import ProductCardRepository
from endpoints.comment import router as comments_router

router = APIRouter()

router.include_router(comments_router)


@router.get("/", response_model=list[OutputProductCardSchema])
async def get_product_cards(
    product_card_repository: ProductCardRepository = Depends(get_product_card_repository),
    limit: int = 100,
    skip: int = 0,
):
    return await ProductCardService(product_card_repository).get_all(limit=limit, skip=skip)


@router.post("/", response_model=OutputProductCardSchema)
async def create_product_card(
    author_id: int,
    data: InputProductCardSchema,
    product_card_repository: ProductCardRepository = Depends(get_product_card_repository),
):
    return await ProductCardService(product_card_repository).create(data=data, author_id=author_id)


@router.patch("/{product_card_id}", response_model=OutputProductCardSchema)
async def update_product_card(
    product_card_id: int,
    data: UpdateProductCardSchema,
    product_card_repository: ProductCardRepository = Depends(get_product_card_repository),
):
    return await ProductCardService(product_card_repository).update(
        product_card_id=product_card_id,
        data=data
    )


@router.delete("/{product_card_id}", status_code=204)
async def delete_product_card(
    product_card_id: int,
    product_card_repository: ProductCardRepository = Depends(get_product_card_repository),
):
    return await ProductCardService(product_card_repository).delete(product_card_id=product_card_id)
