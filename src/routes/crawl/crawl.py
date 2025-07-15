from typing import Annotated

from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from loguru import logger
from pydantic import HttpUrl

from src.core.success import Success
from src.schemas.crawl import CrawlOutSchema
from src.services import get_crawl_service
from src.services.crawl import CrawlService

router = APIRouter(prefix="/crawl", tags=["crawl"])


@router.get(path="")
async def crawl(
    url: Annotated[HttpUrl, Query(...)],
    service: Annotated[CrawlService, Depends(get_crawl_service)],
) -> JSONResponse:
    logger.debug(f"Running crawl {url}")
    out: CrawlOutSchema = await service.crawl(url)
    return Success.ok(
        data=out
    ).to_resp()
