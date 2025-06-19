from typing import Any, Dict

def create_error_response(code: Any, message: str) -> Dict:
    return {
        "status": "error",
        "error": {
            "code": code,
            "message": message
        }
    }