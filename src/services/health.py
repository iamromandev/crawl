from src.core.base import BaseService
from src.core.common import get_app_version
from src.schemas.health import HealthSchema


class HealthService(BaseService):

    def __init__(self) -> None:
        super().__init__()

    async def check_health(self) -> HealthSchema:
        app_version = get_app_version()
        health: HealthSchema = HealthSchema(
            version=app_version,
        )

        return health
