from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

import toml
from pydantic import HttpUrl

from src.core.formats import serialize


def get_base_url(url: HttpUrl) -> HttpUrl:
    """
    Extracts the base URL from a given URL.

    Parameters:
        url (HttpUrl): The full URL.

    Returns:
        HttpUrl: The base URL (scheme + domain).
    """
    parsed_url = urlparse(serialize(url))
    return HttpUrl.build(scheme=parsed_url.scheme, host=parsed_url.netloc, port=parsed_url.port, path="")


def get_app_version() -> str:
    try:
        with open("pyproject.toml") as f:
            data = toml.load(f)
            return data['project']['version']
    except FileNotFoundError:
        return "Version information not found"
    except KeyError:
        return "Version key not found in pyproject.toml"


def get_file_extension_with_dot(filename: str) -> str | None:
    ext = Path(filename).suffix
    return ext


def get_file_extension(filename: str) -> str | None:
    ext = Path(filename).suffix
    file_extension = ext.lstrip('.') if ext else None
    return file_extension


def current_timestamp(format: str = "%Y%m%d%H%M%S") -> str:
    timestamp = datetime.now(UTC).strftime(format)
    return timestamp
