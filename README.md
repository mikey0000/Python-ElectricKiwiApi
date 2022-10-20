# Electric Kiwi Python API

## What it does
Provide a simple API interface to the Electric Kiwi API and includes all endpoints available on the juice hacker site

## What it does not
session management / token management, there are enough libraries and frameworks that
already do this very well, no point reinventing the wheel

Authentication is left to you.


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
