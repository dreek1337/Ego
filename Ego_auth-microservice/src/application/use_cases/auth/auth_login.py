from src.common import BaseUseCase
from src.config import LoginSchema


class UserLoginUseCase(BaseUseCase):
    def __init__(self):
        pass

    async def __call__(self, data: LoginSchema):
        pass
