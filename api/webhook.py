from fastapi import APIRouter

router = APIRouter(prefix="/webhook")

@router.post("/")
async def webhook():

    return {
        "status":"ok"
    }
