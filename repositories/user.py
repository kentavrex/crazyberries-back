from db.models import User
from db.schemas.user import OutputUserSchema
from repositories import BaseRepository


class UserRepository(BaseRepository):
    model = User
    schema = OutputUserSchema
