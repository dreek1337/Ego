from fastapi import Request, FastAPI
from starlette.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException  # type: ignore


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, exception_handler)


def exception_handler(request: Request, exc: AuthJWTException):
    print()
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
