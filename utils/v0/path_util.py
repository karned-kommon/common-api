from fastapi import HTTPException, status
from config.config import DEFAULT_UNPROTECTED_PATH, DEFAULT_UNLICENSED_PATH


def is_unprotected_path( path: str ) -> bool:
    if DEFAULT_UNPROTECTED_PATH == "":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API config is not configured",
        )

    return path.lower() in DEFAULT_UNPROTECTED_PATH

def is_unlicensed_path( path: str ) -> bool:
    if DEFAULT_UNLICENSED_PATH == "":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API config is not configured",
        )

    return path.lower() in DEFAULT_UNLICENSED_PATH