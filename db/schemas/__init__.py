from pydantic import BaseModel


class CustomBase(BaseModel):
    def dict(self, **kwargs):
        """Для конвертации схемы в модель бд необходимо скрыть кастомные поля схемы"""
        hidden_fields = set(
            attribute_name
            for attribute_name, model_field in self.__fields__.items()
            if model_field.field_info.extra.get("hidden") is True
        )
        kwargs.setdefault("exclude", hidden_fields)
        return super().dict(**kwargs)

    class Config:
        orm_mode = True
        use_enum_values = True
