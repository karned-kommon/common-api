from common_api.services.v0 import Logger
from fastapi.middleware.cors import CORSMiddleware

logger = Logger()

class CustomCORSMiddleware(CORSMiddleware):
    def __init__(self, app):
        logger.init("Initializing CustomCORSMiddleware")
        super().__init__(
            app=app,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["Content-Type", "X-License-Key", "Authorization"],
            max_age=600
        )