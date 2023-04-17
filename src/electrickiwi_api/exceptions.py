class ElectricKiwiException(Exception):
    """Base class for all client exceptions."""


class ApiException(ElectricKiwiException):
    """Raised during problems talking to the API."""


class AuthException(ApiException):
    """Raised due to auth problems talking to API."""


class InvalidSyncTokenException(ApiException):
    """Raised when the sync token is invalid."""


class RequestsExceededException(ApiException):
    """Raised when requests exceed 20 requests a second"""
