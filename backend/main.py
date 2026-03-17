from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="QueryMind API")

app.include_router(router)