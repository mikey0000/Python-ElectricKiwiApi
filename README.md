# Electric Kiwi Python API

[![SemVer 0.5.3][img_version]][url_version]
[![PyPI Releases][img_pypi]][url_pypi]
[![Supported Python Versions][img_pyversions]][url_pyversions]

[img_version]: https://img.shields.io/static/v1.svg?label=SemVer&message=0.5.3&color=blue
[url_version]: https://pypi.org/project/electrickiwi-api/

[img_pypi]: https://img.shields.io/badge/PyPI-wheels-green.svg
[url_pypi]: https://pypi.org/project/bumpver/#files

[img_pyversions]: https://img.shields.io/pypi/pyversions/electrickiwi-api.svg
[url_pyversions]: https://pypi.python.org/pypi/electrickiwi-api

## What it does
Provide a simple API interface to the Electric Kiwi API and includes all endpoints available on the juice hacker site

## What it does not
session management / token management, there are enough libraries and frameworks that
already do this very well, no point reinventing the wheel

Authentication has been left to you.


## How to use it

```python
# set env for url
os.environ["ELECTRICKIWI_BASE_URL"] = "https://api-dev.electrickiwi.co.nz"
# your session with a authentication token
client = new ElectricKiwiApi(authentication_method=HeaderAuthentication(token="<secret_value>")) 

# call it
```

### TODO
renew session token by calling the token endpoint
