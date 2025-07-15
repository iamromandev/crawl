from loguru import logger
from pydantic import HttpUrl

from src.core.base import BaseService
from src.core.clients import PlaywrightClient
from src.schemas.crawl import CrawlOutSchema


class CrawlService(BaseService):
    _playwright_client: PlaywrightClient

    def __init__(
        self,
        playwright_client: PlaywrightClient,
    ) -> None:
        super().__init__()
        self._playwright_client = playwright_client

    async def crawl(self, url: HttpUrl) -> CrawlOutSchema:
        logger.debug(f"{self._tag}|crawl(): Starting crawl for {url}")
        html: str = await self._playwright_client.get_html(url)
        extracted_urls: list[HttpUrl] | None = await self._playwright_client.get_urls(url)

        return CrawlOutSchema(
            html=html,
            urls=extracted_urls
        )
