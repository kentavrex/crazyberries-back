import logging

from databases import Database
from minio import Minio

from config import MINIO_CLIENT_SECRET_KEY, MINIO_CLIENT_ACCESS_KEY
from db.schemas import CustomBase
from errors import NotFoundError

logger = logging.getLogger(__name__)


class BaseRepository:
    model = None
    schema = None

    def __init__(self, database: Database):
        self.database = database

    async def get_all(self, limit: int = 100, skip: int = 0) -> list[schema]:
        query = self.model.select().limit(limit).offset(skip)
        db_response = await self.database.fetch_all(query=query)
        return [self.schema.from_orm(obj) for obj in db_response]

    async def get_by_id(self, object_id: int) -> schema:
        query = self.model.select().where(self.model.c.id == object_id)
        obj = await self.database.fetch_one(query=query)
        if obj is None:
            raise NotFoundError(f"'{self.model.__name__}' object not found")
        return self.schema.from_orm(obj)

    async def create(self, data: CustomBase) -> schema:
        query = self.model.insert().values(**data.dict())
        try:
            element_created = await self.database.execute(query)
        except Exception as e:
            logger.error(str(e))
            raise ValueError("Wrong data passed")

        return self.schema.from_orm(element_created)

    async def update(self, object_id: int, data: CustomBase) -> schema:
        query = self.model.update().where(self.model.c.id == object_id).values(**data.dict())
        try:
            obj = await self.database.execute(query)
        except Exception as e:
            logger.error(str(e))
            raise ValueError("Wrong data passed")

        return self.schema.from_orm(obj)

    async def delete(self, object_id: int):
        query = self.model.delete().where(self.model.c.id == object_id)
        await self.database.execute(query=query)


bucket_name = "crazyberries-data"
client = Minio(
    endpoint="minio",
    access_key=MINIO_CLIENT_ACCESS_KEY,
    secret_key=MINIO_CLIENT_SECRET_KEY,
)
