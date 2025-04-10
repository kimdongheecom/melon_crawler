from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from .api.melon.melon_router import router as melon_router




app = FastAPI(title="Melon API")
api_router = APIRouter(prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Melon API"}

app.include_router(melon_router)