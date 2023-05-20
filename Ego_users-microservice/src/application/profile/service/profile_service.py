from src.application.profile.interfaces.repository.profile_repository import ProfileRepo


class ProfileServile:
    def __init__(
            self,
            *,
            profile_repo: ProfileRepo,
            uow:
    ) -> None:
        ...

    async def get_profile(self):
        ...
