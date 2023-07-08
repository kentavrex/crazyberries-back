"""Data validation and settings management"""
from db.schemas import CustomBase


class BaseUserSchema(CustomBase):
    login: str
    name: str
    location: str | None = None


class OutputUserSchema(BaseUserSchema):
    id: int | None = None


class InputUserSchema(BaseUserSchema):
    """Class for data that user gives"""

    pass


class UpdateUserSchema(InputUserSchema):
    login: str | None
    name: str | None
    location: str | None = None


class CreateUserSchema(InputUserSchema):
    pass
