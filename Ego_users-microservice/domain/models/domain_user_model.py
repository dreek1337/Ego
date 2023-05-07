from datetime import date
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """
    Полная модель пользователя
    """
    id: int | None = Field(None, 'Идентификатор пользователя')
    username: str = Field(..., 'Никнейм пользователя в сервисе')
    email: EmailStr = Field(..., 'Почта для пользователя')
    password: str | None = Field(None, 'Пароль пользователя')
    birthday: date | None = Field(None, 'День рождения пользователя')
    registration_date: date = Field(..., 'Дата регистрации пользователя')
    is_active: bool = Field(..., 'Значение об активности пользователя')
    rights: str = Field(..., 'Права пользователя')
    photo_id: int | None = Field(None, 'АЙди фотографии пользователя')
