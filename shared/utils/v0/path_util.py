from shared.config import UNPROTECTED_PATH, UNLICENSED_PATH


def is_unprotected_path( path: str ) -> bool:
    return path.lower() in UNPROTECTED_PATH

def is_unlicensed_path( path: str ) -> bool:
    return path.lower() in UNLICENSED_PATH