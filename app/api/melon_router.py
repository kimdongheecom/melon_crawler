from fastapi import APIRouter

router = APIRouter(prefix="/melon")

@router.get("/")
async def get_melon():
    pass

@router.post("/")
async def create_melon():
    pass

@router.put("/{melon_id}")
async def update_melon(melon_id: int):
    pass

@router.delete("/{melon_id}")
async def delete_melon(melon_id: int):
    pass 