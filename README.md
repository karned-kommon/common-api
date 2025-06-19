# Shared

A collection of shared FastAPI middlewares and decorators for Karned applications.

## Installation

You can install this package using pip:

```bash
pip install git+https://github.com/karned-kommon/shared.git
```

This will automatically install all required dependencies (fastapi, starlette, httpx, redis).

## Alternative Installation

If you prefer to install dependencies manually, you can clone the repository and install the dependencies:

```bash
git clone https://github.com/karned-kommon/shared.git
cd shared
pip install -r requirements.txt
pip install -e .
```

## Components

This package includes the following components:

### Middlewares

- **TokenVerificationMiddleware**: Verifies JWT tokens from Keycloak
- **LicenceVerificationMiddleware**: Verifies license keys for API access
- **CorsMiddleware**: Handles Cross-Origin Resource Sharing (CORS)
- **ExceptionHandler**: Provides standardized exception handling

### Decorators

- **check_permissions**: Checks if a user has the required permissions
- **log_time**: Logs the execution time of functions and methods

### Models

- **ResponseModel**: Standardized response model for API responses

### Services

- **InMemoryService**: Provides Redis functionality for caching

### Utilities

- **PathUtil**: Utility functions for path handling and validation

## Usage

Import the middlewares and decorators in your FastAPI application:

```python
from fastapi import FastAPI, Request
from middlewares.v0.token_middleware import TokenVerificationMiddleware
from middlewares.v0.licence_middleware import LicenceVerificationMiddleware
from middlewares.v0.cors_middleware import CorsMiddleware
from middlewares.v0.exception_handler import ExceptionHandlerMiddleware
from decorators.v0.check_permission import check_permissions
from decorators.v0.log_time import log_time, log_time_async

app = FastAPI()

# Add middlewares
app.add_middleware(TokenVerificationMiddleware)
app.add_middleware(LicenceVerificationMiddleware)
app.add_middleware(CorsMiddleware)
app.add_middleware(ExceptionHandlerMiddleware)

# Use decorators
@app.get("/protected-route")
@check_permissions(["read"])
async def protected_route(request: Request):
    return {"message": "You have access to this route"}

@log_time
def my_function():
    # This function's execution time will be logged
    pass

@log_time_async
async def my_async_function():
    # This async function's execution time will be logged
    pass
```

## Note on Dependencies

This package relies on several internal modules that should be provided by your FastAPI application:

- `services.v0.inmemory_service`: Provides Redis functionality
- `decorators.v0.log_time`: Provides timing decorators
- `utils.v0.path_util`: Provides path utility functions

Make sure these modules are available in your application's Python path.

## Configuration

This package has been designed to work without direct dependencies on a specific `config.config` module. All default variables are stored in the `config/config.py` file. You can provide configuration values in two ways:

### 1. Pass configuration values directly to the middlewares and decorators

```python
from fastapi import FastAPI
from middlewares.v0.token_middleware import TokenVerificationMiddleware
from middlewares.v0.licence_middleware import LicenceVerificationMiddleware
from decorators.v0.check_permission import check_permissions

app = FastAPI()

# Configure TokenVerificationMiddleware with your Keycloak settings
app.add_middleware(
    TokenVerificationMiddleware,
    keycloak_host="https://your-keycloak-host",
    keycloak_realm="your-realm",
    keycloak_client_id="your-client-id",
    keycloak_client_secret="your-client-secret"
)

# Configure LicenceVerificationMiddleware with your API gateway URL
app.add_middleware(
    LicenceVerificationMiddleware,
    url_api_gateway="https://your-api-gateway"
)

# Configure check_permissions decorator with your API name
@app.get("/protected-route")
@check_permissions(["read"], api_name="your-api-name")
async def protected_route(request: Request):
    return {"message": "You have access to this route"}
```

### 2. Set environment variables

If you don't provide configuration values directly, the package will look for the following environment variables:

- `KEYCLOAK_HOST`: The URL of your Keycloak server
- `KEYCLOAK_REALM`: The Keycloak realm to use
- `KEYCLOAK_CLIENT_ID`: The Keycloak client ID
- `KEYCLOAK_CLIENT_SECRET`: The Keycloak client secret
- `URL_API_GATEWAY`: The URL of your API gateway
- `API_NAME`: The name of your API

You can set these environment variables in your application's environment or in a `.env` file.
