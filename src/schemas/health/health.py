from typing import Annotated

from pydantic import Field

from src.core.base import BaseSchema


class HealthSchema(BaseSchema):
    version: Annotated[str, Field(default="0.0.0", description="Application version")]
