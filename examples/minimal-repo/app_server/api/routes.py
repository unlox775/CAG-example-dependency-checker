"""FastAPI route handlers."""

from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter()


class ExportRequest(BaseModel):
    format: str = "csv"


@router.post("/export")
async def trigger_export(req: ExportRequest):
    """Trigger an export (stub). In production would enqueue job."""
    return {"status": "queued", "format": req.format}


@router.get("/external")
async def fetch_external():
    """Fetch from external API using httpx."""
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")
        return r.json()
