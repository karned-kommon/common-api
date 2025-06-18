import os

# Default values that can be overridden
DEFAULT_URL_API_GATEWAY = os.environ.get("URL_API_GATEWAY", "")
DEFAULT_KEYCLOAK_HOST = os.environ.get("KEYCLOAK_HOST", "")
DEFAULT_KEYCLOAK_REALM = os.environ.get("KEYCLOAK_REALM", "")
DEFAULT_KEYCLOAK_CLIENT_ID = os.environ.get("KEYCLOAK_CLIENT_ID", "")
DEFAULT_KEYCLOAK_CLIENT_SECRET = os.environ.get("KEYCLOAK_CLIENT_SECRET", "")
DEFAULT_API_NAME = os.environ.get("API_NAME", "")