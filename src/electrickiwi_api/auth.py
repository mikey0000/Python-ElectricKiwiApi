"""abstract auth implementation for electric kiwi"""
from __future__ import annotations

import logging
from abc import abstractmethod, ABC
from typing import Any, Mapping, Optional

from aiohttp import ClientSession, ClientResponse, ClientError

from electrickiwi_api.exceptions import AuthException

AUTHORIZATION_HEADER = "Authorization"

_LOGGER = logging.getLogger(__name__)

API_BASE_URL = "https://api-dev.electrickiwi.co.nz"


class AbstractAuth(ABC):
    """Abstract class to make authenticated requests."""

    def __init__(self, websession: ClientSession, host: str):
        """Initialize the auth."""
        self._websession = websession
        self._host = host if host is not None else API_BASE_URL

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def request(self, method: str, url: str, **kwargs: Optional[Mapping[str, Any]]) -> ClientResponse:
        """Make a request."""
        try:
            access_token = await self.async_get_access_token()
        except ClientError as err:
            raise AuthException(f"Access token failure: {err}") from err
        headers = {AUTHORIZATION_HEADER: f"Bearer {access_token}"}
        if not (url.startswith("https://")):
            url = f"{self._host}{url}"
        _LOGGER.debug("request[%s]=%s %s", method, url, kwargs.get("params"))
        if method == "post" and "json" in kwargs:
            _LOGGER.debug("request[post json]=%s", kwargs["json"])
        return await self._websession.request(method, url, **kwargs, headers=headers)
