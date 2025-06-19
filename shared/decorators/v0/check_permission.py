from fastapi import Request
from functools import wraps
from typing import List

from shared.services.v0 import check_user_has_permissions

def check_permissions(permissions: List[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            check_user_has_permissions(request, permissions)
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator