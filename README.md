<h1>EGO</h1>

<h3>Архетиктура сервиса</h3>

![alt text](https://sun9-71.userapi.com/impg/BAO9NoMLWJkVN-cieiTrhuOIXQzp6LtvCC372g/tvNiEiPjCPs.jpg?size=1111x899&quality=96&sign=6ce5d0d87be548442dc9e87babb773ea&type=album)

<h3>Стэк</h3>

- FastAPI

- SQLAlchemy/PostgreSQL

- Minio/Aiobotocore

- Elasticsearch (Kibana, Curator)

- Docker/Docker compose

- pytest (Unit-тесты)

- mypy, black, isort, ruff

- CI (pre-commit, GitHub Actions)

- Apache APISIX

<h3>Архетиктура</h3>

- Микросервисы

- DDD

<h3>Запуск проекта</h3>

```
bash startup.sh
```

<h3>Swagger-UI</h3>

![alt text](https://sun9-79.userapi.com/impg/X_1zgW6V1j1SVRvsDahf2foHvxLbL8DFDeya-Q/ZfK7z4AdV24.jpg?size=1280x636&quality=96&sign=1ce2cd48110e66267e3c78831674f62f&type=album)

<h3>Endpoints</h3>

*Регистрация*

```
ВАЖНО!
1. Вставьте актуальный адрес APISIX сервиса.
2. Осуществляйте запросы на данный момент через Postman или терминал.
```

1. Зарегестрируйте почту, логин и пароль(Получите JWT токен и используйте его в заголовке Authorization).
<h4>POST auth/registration</h4>

```
curl -X 'POST' \
  'http://example.com/auth/registration' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "testusername",
  "password": "testpassword",
  "user_email": "testemail@example.com"
}'
```

2. Закончите регистрацию в сервисе.

```
curl -X 'POST' \
  'http://example.com/users/create_user' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <JWT Token>
  -d '{
  "first_name": "Test",
  "last_name": "Test",
  "gender": "male",
  "birthday": "2023-07-18"
}'
```

*Создайте свой первый пост*

```
curl -X 'POST' \
  'http://example.com/posts/create_post' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text_content": "My test text post!"
}'
```

<h3>TODO</h3>

- Сделать сервис для маршрутов в шлюзе, с плагином forward-auth

- Натсроить добавление заголовка в запрос в OpenAPI для jwt

- Сделать логирование

- Добавить кеширование через Redis

- Настроить nginx
