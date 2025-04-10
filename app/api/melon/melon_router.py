from fastapi import APIRouter

from app.domain.melon.services.melon_services import fetch_melon_chart

router = APIRouter(prefix="/melon", tags=["melon"])

@router.get("/")
async def get_melon():
    pass

@router.get("/chart")
async def get_melon_chart():
    results = await fetch_melon_chart()
    for song in results:
        print(f"{song['rank']}위 | 제목: {song['title']} | 아티스트: {song['artist']} | 앨범: {song['album']}")
    return {"message": "콘솔 출력 완료", "count": len(results)}


@router.post("/")
async def create_melon():
    pass

@router.put("/{melon_id}")
async def update_melon(melon_id: int):
    pass

@router.delete("/{melon_id}")
async def delete_melon(melon_id: int):
    pass 