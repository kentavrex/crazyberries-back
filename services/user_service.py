from repositories.user import UserRepository
from db.schemas.user import OutputUserSchema, CreateUserSchema, UpdateUserSchema


class UsersService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def get_all(self, limit: int, skip: int) -> list[OutputUserSchema]:
        return self.repository.get_all(limit, skip)

    async def get_by_id(self, user_id: int) -> OutputUserSchema:
        return self.repository.get_by_id(user_id)

    async def create(self, data: CreateUserSchema) -> OutputUserSchema:
        return self.repository.create(data)

    async def update(self, user_id: int, data: UpdateUserSchema) -> OutputUserSchema:
        return self.repository.update(user_id, data)

    async def delete(self, user_id: int):
        return self.repository.delete(user_id)
