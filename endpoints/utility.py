from fastapi import APIRouter

from services.utility_service import UtilityService

router = APIRouter()


@router.get("/categories", response_model=list[str])
def get_categories():
    return UtilityService.get_categories()
