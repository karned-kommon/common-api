API_NAME = None
URL_API_GATEWAY = None
KEYCLOAK_HOST = None
KEYCLOAK_REALM = None
KEYCLOAK_CLIENT_ID = None
KEYCLOAK_CLIENT_SECRET = None
UNPROTECTED_PATH = None
UNLICENSED_PATH = None
REDIS_DB = None
REDIS_HOST = None
REDIS_PORT = None
REDIS_PASSWORD = None

def init_config(
        api_name: str,
        url_api_gateway: str,
        keycloak_host: str,
        keycloak_realm: str,
        keycloak_client_id: str,
        keycloak_client_secret: str,
        unprotected_path: str,
        unlicensed_path: str,
        redis_db: int,
        redis_host: str,
        redis_port: int,
        redis_password: str
):
    global API_NAME
    global URL_API_GATEWAY
    global KEYCLOAK_HOST
    global KEYCLOAK_REALM
    global KEYCLOAK_CLIENT_ID
    global KEYCLOAK_CLIENT_SECRET
    global UNPROTECTED_PATH
    global UNLICENSED_PATH
    global REDIS_DB
    global REDIS_HOST
    global REDIS_PORT
    global REDIS_PASSWORD

    API_NAME = api_name
    URL_API_GATEWAY = url_api_gateway
    KEYCLOAK_HOST = keycloak_host
    KEYCLOAK_REALM = keycloak_realm
    KEYCLOAK_CLIENT_ID = keycloak_client_id
    KEYCLOAK_CLIENT_SECRET = keycloak_client_secret
    UNPROTECTED_PATH = unprotected_path
    UNLICENSED_PATH = unlicensed_path
    REDIS_DB = redis_db
    REDIS_HOST = redis_host
    REDIS_PORT = redis_port
    REDIS_PASSWORD = redis_password

