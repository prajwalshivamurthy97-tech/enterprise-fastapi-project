from fastapi import FastAPI

from app.api.user_routes import router as user_router
from app.database.session import init_db

app = FastAPI(title="Enterprise FastAPI Project")

init_db()

app.include_router(user_router)


@app.get("/")
def home():
    return {"message": "App is running"}