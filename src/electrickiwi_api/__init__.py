# __init__.py

# version of ElectricKiwiApi for Python
__version__ = "0.6.0"

from electrickiwi_api.api import (
    ElectricKiwiEndpoint,
    ElectricKiwiApi
)

from electrickiwi_api.auth import (
    AbstractAuth
)

# remove dev for production
# Authorization URL 	https://welcome-dev.electrickiwi.co.nz/oauth/authorize
# Token URL 	https://welcome-dev.electrickiwi.co.nz/oauth/token
# API 	https://api-dev.electrickiwi.co.nz
