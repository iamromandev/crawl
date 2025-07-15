from functools import cached_property

from pydantic import Field, WebsocketUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from .types import Env


class Settings(BaseSettings):
    # core
    env: Env = Field(...)
    debug: bool = Field(...)
    # playwright
    playwright_connection: str = Field(...)
    playwright_host: str = Field(...)
    playwright_port: int = Field(...)
    playwright_headless: bool = Field(...)
    playwright_user_agent: str = Field(...)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )

    @cached_property
    def is_local(self) -> bool:
        return self.env == Env.LOCAL

    @cached_property
    def is_prod(self) -> bool:
        return self.env == Env.PROD

    @cached_property
    def playwright_url(self) -> WebsocketUrl:
        return WebsocketUrl.build(
            scheme=self.playwright_connection,
            host=self.playwright_host,
            port=self.playwright_port,
        )


settings = Settings()
