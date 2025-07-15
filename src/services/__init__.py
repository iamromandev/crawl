from collections.abc import AsyncGenerator

from fastapi import Depends

from src.core.clients import PlaywrightClient, get_playwright_client
from src.core.config import settings

from .crawl import CrawlService
from .health import HealthService


async def get_health_service(
) -> AsyncGenerator[HealthService]:
    yield HealthService( )


async def get_crawl_service(
    playwright_client: PlaywrightClient = Depends(get_playwright_client),

) -> AsyncGenerator[CrawlService]:
    yield CrawlService(
        playwright_client,
  
    )
