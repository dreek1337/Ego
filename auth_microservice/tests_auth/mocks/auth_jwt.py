from fastapi_jwt_auth import AuthJWT  # type: ignore


class AuthJWTMock(AuthJWT):
    def __init__(self) -> None:
        self.ref_token = "bad_refresh"
        self.acc_token = "bad_token"

        super().__init__()

    def set_refresh_token(self, ref_token: str) -> None:
        """
        Установка рефреш токена
        """
        self.ref_token = ref_token

    def set_access_token(self, acc_token: str) -> None:
        """
        Установка ацесс токена

        """
        self.acc_token = acc_token
