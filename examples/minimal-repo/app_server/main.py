"""App server entrypoint."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from dotenv import load_dotenv
import structlog

from db.connection import init_db
from jobs.scheduler import get_scheduler
from api.routes import router as api_router

load_dotenv()
logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    scheduler = get_scheduler()
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix="/api", tags=["api"])


@app.get("/health")
async def health():
    return {"status": "ok", "service": "app_server"}
