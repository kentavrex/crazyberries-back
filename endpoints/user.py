from fastapi import APIRouter, Depends

from db.schemas.user import OutputUserSchema, CreateUserSchema, UpdateUserSchema
from repositories.user import UserRepository
from endpoints import get_user_repository
from services.user_service import UsersService


router = APIRouter()


@router.get("/", response_model=list[OutputUserSchema])
async def get_users(
    users_repository: UserRepository = Depends(get_user_repository),
    limit: int = 100,
    skip: int = 0,
):
    return await UsersService(users_repository).get_all(limit=limit, skip=skip)


@router.get("/{user_id}", response_model=OutputUserSchema)
async def get_user(user_id: int, users_repository: UserRepository = Depends(get_user_repository)):
    return await UsersService(users_repository).get_by_id(user_id=user_id)


@router.post("/", response_model=OutputUserSchema)
async def create_user(data: CreateUserSchema, users_repository: UserRepository = Depends(get_user_repository)):
    return await UsersService(users_repository).create(data=data)


@router.patch("/{user_id}", response_model=OutputUserSchema)
async def update_user(
    user_id: int, data: UpdateUserSchema, users_repository: UserRepository = Depends(get_user_repository)
):
    return await UsersService(users_repository).update(user_id=user_id, data=data)


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, users_repository: UserRepository = Depends(get_user_repository)):
    return await UsersService(users_repository).delete(user_id)
