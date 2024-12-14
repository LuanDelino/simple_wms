from fastapi import FastAPI
from contextlib import asynccontextmanager
from infra.database import engine
from infra.create_tables import create_tables
from infra.configs import settings
from routes import api_router


app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables(engine)
    yield


app.include_router(api_router, prefix=settings.API_V1_STR)
