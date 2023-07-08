from db import database
from repositories.user import UserRepository
from repositories.product_card import ProductCardRepository
from repositories.comment import CommentsRepository


def get_user_repository() -> UserRepository:
    return UserRepository(database)


def get_product_card_repository() -> ProductCardRepository:
    return ProductCardRepository(database)


def get_comments_repository() -> CommentsRepository:
    return CommentsRepository(database)
