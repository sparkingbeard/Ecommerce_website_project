from fastapi import APIRouter
from services.payments_service import create_order
from fastapi import Request

router = APIRouter()
@router.post("/")
async def create_order(request: Request):
    body = await request.json()
    amount_in_paise = body["amount"] * 100
    order = create_order(amount_in_paise)
    return {{"order_id": order.id, "amount": order.amount}}