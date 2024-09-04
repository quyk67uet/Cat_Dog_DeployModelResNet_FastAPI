import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from utils.logger import Logger

LOGGER = Logger(__file__, log_file="http.log")
class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response: Response = await call_next(request)
        process_time = time.time() - start_time
        LOGGER.log.info(
            f"{request.client.host} - \"{request.method} {request.url.path} {request.scope['http_version']}\" "
            f"{response.status_code} {process_time:.2f}s"
        )
        return response
