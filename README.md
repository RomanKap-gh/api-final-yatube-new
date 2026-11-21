# REST Api Yatube
REST Api для платформы для блогов Yatube, в котором можно создавать посты, добавлять комментарии, подписываться на других авторов.
## Функционал

* Регистрация и аутентификация полльзователей (JWT + Djoser)
* Просмотр постов авторов
* Создание, редактирование и удаление постов только для зарегистрированных пользователей
* Создание, редактирование и удаление комментарийв к постам только для зарегистрированных пользователей
* Подписка на других пользователей с поиском по списку подписок

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/RomanKap-gh/api-final-yatube-new.git
```

```
cd api-final-new
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
```
cd yatube_api
```
Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Примеры запросов

### Аутентификация

Регистрация нового пользователя:
```
POST /auth/users/
Content-Type: application/json

{
    "username": "newuser",
    "password": "strongpassword123",
    "email": "newuser@example.com"
}
```
*Ответ (201 Created):*
```
{
    "email": "newuser@example.com",
    "username": "newuser",
    "id": 2
}
```
Получение JWT-токена:
```
POST /auth/jwt/create/
Content-Type: application/json

{
    "username": "newuser",
    "password": "strongpassword123"
}
```
*Ответ (200 ОК):*
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
```
При всех последующих запросах, требующих аутентификации, необходимо в загловке с ключом *Authorization* передавать токен:
```
Bearer <ваш_access_токен>
```
### Посты (Posts)
Создание поста (только для авторизованных пользователей):
```
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "text": "Ваш пост",
    "group": 1
}
```
*Ответ (201 Created):*
```
{
    "id": 1,
    "author": "newuser",
    "text": "Ваш пост",
    "pub_date": "2026-11-21T12:00:00Z",
    "image": null,
    "group": 1
}
```
Получение списка постов (С пагинацией):
```
GET /api/v1/posts/?limit=5&offset=0
```
*Ответ (200 ОК):*
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "newuser",
            "text": "Ваш пост",
            "pub_date": "2026-11-21T12:00:00Z",
            "image": null,
            "group": 1
        }
    ]
}
```
### Комментарии (Comments)
Добавление комментария к посту:
```
POST /api/v1/posts/1/comments/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "text": "Ваш комментарий"
}
```
*Ответ (201 Created):*
```
{
    "id": 1,
    "author": "newuser",
    "post": 1,
    "text": "Отличный пост!",
    "created": "2026-11-21T12:05:00Z"
}
```
### Подписки (Follow)
Подписаться на пользователя:
```
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "following": "another_user"
}
```
*Ответ (201 Created):*
```
{
    "user": "your username",
    "following": "another_user"
}
```
Поиск подписок (с фильтром):
```
GET /api/v1/follow/?search=another
Authorization: Bearer <access_token>
```
*Ответ (200 ОК):*
```
[
    {
        "user": "your username",
        "following": "another_user"
    }
]
```
