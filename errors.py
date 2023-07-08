from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class NotFoundError(Exception):
    pass


class HandleHTTPErrorsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
        except NotFoundError as e:
            return JSONResponse(status_code=404, content={"detail": str(e)})
        except ValueError as e:
            return JSONResponse(status_code=400, content={"detail": str(e)})
        except Exception:
            return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
        return response
