from functools import cached_property
from typing import Annotated, Any

from fastapi.encoders import jsonable_encoder
from loguru import logger
from pydantic import BaseModel, ConfigDict, Field


# schema - request + response + validation
class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    @cached_property
    def _tag(self) -> str:
        return self.__class__.__name__

    def to_json(self, exclude_none: bool = True) -> Any:
        json = jsonable_encoder(self, exclude_none=exclude_none)
        logger.info(f"{self._tag}|to_json(): {json}")
        return json

    def to_dict(
        self,
        exclude_fields: Annotated[set[str] | None, Field(...)] = None,
        exclude_none: Annotated[bool, Field(...)] = None,
        exclude_unset: Annotated[bool, Field(...)] = None,
    ) -> dict[str, Any]:
        data = self.model_dump(
            exclude=exclude_fields,
            exclude_none=exclude_none,
            exclude_unset=exclude_unset
        )
        logger.info(f"{self._tag}|to_dict(): {data}")
        return data

    def safe_dump(
        self, exclude_fields: Annotated[set[str] | None, Field(...)] = None,
    ) -> dict[str, Any]:
        data = self.to_dict(
            exclude_fields=exclude_fields,
            exclude_none=True,
            exclude_unset=True
        )
        logger.info(f"{self._tag}|to_dict(): {data}")
        return data

    def log(self) -> None:
        data = self.model_dump()
        logger.info(f"{self._tag}|log(): {data}")


# service
class BaseService:

    def __init__(self) -> None:
        logger.debug(f"{self._tag}|__init__()")

    @cached_property
    def _tag(self) -> str:
        return self.__class__.__name__
