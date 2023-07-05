from typing import Any, Callable, TypeVar

FromModel = TypeVar("FromModel", bound=Any)
ToModel = TypeVar("ToModel", bound=Any)


class Convert:
    """
    Класс который содержит в себе логику преобразования данных
    """

    def __init__(
        self,
        *,
        from_model: type[FromModel],
        to_model: type[ToModel],
        loader: Callable[[FromModel], ToModel],
    ) -> None:
        self.from_model = from_model
        self.to_model = to_model
        self.loader = loader

    def load(self, from_model: FromModel) -> Any:
        """
        Преобразование данных
        """
        return self.loader(from_model)

    def check(self, *, from_model: type[FromModel], to_model: type[ToModel]) -> bool:
        """
        Проверка на подходящий Convert
        """
        return from_model == self.from_model and to_model == self.to_model
