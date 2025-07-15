from typing import Annotated

from pydantic import Field, HttpUrl

from src.core.base import BaseSchema


class CrawlOutSchema(BaseSchema):
    html: Annotated[str | None, Field(default=None)]
    urls: Annotated[list[HttpUrl] | None, Field(default=None)]
