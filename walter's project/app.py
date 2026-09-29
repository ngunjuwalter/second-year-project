from fastapi import FastAPI
from contextlib import asynccontextmanager

from db.base import Base
from db.session import engine
from db.seed import insert_sample_data
from routes import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown events.
    """
    Base.metadata.create_all(bind=engine)
    insert_sample_data()
    yield


app = FastAPI(
    title="ONSIGHT Fraud Detection API",
    lifespan=lifespan
)

app.include_router(users.router)
