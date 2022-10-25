import aiohttp
from typing import Any, cast

from aiohttp import ClientSession

from electrickiwi_api.auth import AbstractAuth
from electrickiwi_api.api import ElectricKiwiApi


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


async def test():
    async with ClientSession() as session:
        api = ElectricKiwiApi(ApiAuthImpl(session, ""))
        await api.get_active_session()
        print("Success")


async def main():
    print("start\n")
    await test()
