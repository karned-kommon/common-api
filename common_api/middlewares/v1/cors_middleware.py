from common_api.services.v0 import Logger
from starlette.middleware.cors import CORSMiddleware as StarletteCorsMW

logger = Logger()

class CORSMiddleware(StarletteCorsMW):
    def __init__(self, app):
        logger.init("Initializing CORSMiddleware")
        super().__init__(
            app=app,
            allow_methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"],
            allow_headers=["*"],
            expose_headers=["Content-Type", "X-License-Key", "Authorization"],
            max_age=600
        )