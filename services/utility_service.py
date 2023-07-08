from db.helpers import ProductCardCategory


class UtilityService:
    @staticmethod
    def get_categories() -> list[str]:
        """Get list of the categories"""
        return [category.value for category in ProductCardCategory]
