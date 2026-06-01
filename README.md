Cinema API
Учебный проект по дисциплине
«Инструментальные средства разработки программного обеспечения».

Описание
REST API для управления кинотеатром.
Позволяет работать с фильмами, актёрами и сеансами.

Проект реализован на Django и Django REST Framework.
В качестве базы данных используется PostgreSQL.

Функциональность
Получение списка объектов
Получение одного объекта по id
Создание объектов
Обновление (PUT и PATCH)
Удаление
Фильтрация фильмов по названию
Фильтрация сеансов по фильму
JWT-авторизация
Swagger документация
Эндпоинты
Актёры
GET /api/v1/actors/ — список актёров
GET /api/v1/actors/{id}/ — информация об актёре
POST /api/v1/actors/ — создание актёра
PUT /api/v1/actors/{id}/ — полное обновление
PATCH /api/v1/actors/{id}/ — частичное обновление
DELETE /api/v1/actors/{id}/ — удаление
Фильмы
GET /api/v1/movies/ — список фильмов
GET /api/v1/movies/{id}/ — информация о фильме
GET /api/v1/movies/?title=название — фильтрация по названию
POST /api/v1/movies/ — создание фильма
PUT /api/v1/movies/{id}/ — полное обновление
PATCH /api/v1/movies/{id}/ — частичное обновление
DELETE /api/v1/movies/{id}/ — удаление
Сеансы
GET /api/v1/sessions/ — список сеансов
GET /api/v1/sessions/{id}/ — информация о сеансе
GET /api/v1/sessions/?movie_id=1 — фильтрация по фильму
POST /api/v1/sessions/ — создание сеанса
PUT /api/v1/sessions/{id}/ — полное обновление
PATCH /api/v1/sessions/{id}/ — частичное обновление
DELETE /api/v1/sessions/{id}/ — удаление
Документация API
Swagger UI:
http://127.0.0.1:8000/api/schema/swagger-ui/

Запуск проекта
Создать виртуальное окружение:
python -m venv venv

Активировать окружение:
venv\Scripts\activate

Установить зависимости:
pip install -r requirements.txt

Настроить подключение к PostgreSQL в settings.py

Выполнить миграции:
python manage.py migrate

Создать суперпользователя:
python manage.py createsuperuser

Запустить сервер:
python manage.py runserver

Используемые технологии
Python
Django
Django REST Framework
PostgreSQL
psycopg2-binary
drf-spectacular
JWT (SimpleJWT)