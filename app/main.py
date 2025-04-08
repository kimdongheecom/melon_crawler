from fastapi import FastAPI, APIRouter

app = FastAPI(title="Melon API")
api_router = APIRouter(prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Melon API"}

app.include_router(api_router) 