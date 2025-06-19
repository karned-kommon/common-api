import redis

from fastapi import HTTPException, status
from shared.config import DEFAULT_REDIS_DB, DEFAULT_REDIS_HOST, DEFAULT_REDIS_PASSWORD, DEFAULT_REDIS_PORT


def get_redis_api_db():
    if DEFAULT_REDIS_HOST == "" or DEFAULT_REDIS_PASSWORD == "" or DEFAULT_REDIS_PORT == "" or DEFAULT_REDIS_DB == "":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API config is not configured",
        )

    return redis.Redis(
        host=DEFAULT_REDIS_HOST,
        db=DEFAULT_REDIS_DB,
        port=DEFAULT_REDIS_PORT,
        password=DEFAULT_REDIS_PASSWORD,
        decode_responses=True
    )

r = get_redis_api_db()