import aiohttp
from typing import Any, cast

from src.electrickiwi_api import AbstractAuth, ElectricKiwiApi


class ApiAuthImpl(AbstractAuth):
    """Authentication implementation for google calendar api library."""

    def __init__(
            self,
            websession: aiohttp.ClientSession,
            token,
    ) -> None:
        """Init the Google Calendar client library auth implementation."""
        super().__init__(websession)
        self._token = token

    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

        return cast(str, self._token)


# headers = {"Authorization": "Bearer eyJh...0M30"}
# async with ClientSession(headers=headers) as session:
# ElectricKiwiApi(ApiAuthImpl(session, token))
