from fastapi_jwt_auth import AuthJWT  # type: ignore


class TokenMakerBase:
    def __init__(self, authorize: AuthJWT):
        self._authorize = authorize
