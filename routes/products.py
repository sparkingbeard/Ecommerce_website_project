from fastapi import APIRouter
from services.products import get_products_service

router = APIRouter()
@router.get("/")
def get_products():
    res = get_products_service()
    return res