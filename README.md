# Cinema API

Учебный проект по дисциплине  
«Инструментальные средства разработки программного обеспечения».

## Описание

REST API для управления кинотеатром.  
Реализована работа с фильмами, актёрами и сеансами.

Проект разработан с использованием Django и Django REST Framework.  
В качестве базы данных используется PostgreSQL.

---

## Функциональность

- Получение списка объектов
- Получение одного объекта по ID
- Создание объектов
- Полное обновление (PUT)
- Частичное обновление (PATCH)
- Удаление
- Фильтрация фильмов по названию
- Фильтрация сеансов по фильму
- JWT‑авторизация
- Swagger документация

---

## Эндпоинты

### Актёры
- GET /api/v1/actors/
- GET /api/v1/actors/{id}/
- POST /api/v1/actors/
- PUT /api/v1/actors/{id}/
- PATCH /api/v1/actors/{id}/
- DELETE /api/v1/actors/{id}/

### Фильмы
- GET /api/v1/movies/
- GET /api/v1/movies/{id}/
- GET /api/v1/movies/?title=название
- POST /api/v1/movies/
- PUT /api/v1/movies/{id}/
- PATCH /api/v1/movies/{id}/
- DELETE /api/v1/movies/{id}/

### Сеансы
- GET /api/v1/sessions/
- GET /api/v1/sessions/{id}/
- GET /api/v1/sessions/?movie_id=1
- POST /api/v1/sessions/
- PUT /api/v1/sessions/{id}/
- PATCH /api/v1/sessions/{id}/
- DELETE /api/v1/sessions/{id}/

---

## Документация API

Swagger UI доступен по адресу:  
http://127.0.0.1:8000/api/schema/swagger-ui/

---

## Установка и запуск

1. Создать виртуальное окружение:
python -m venv venv

2. Активировать окружение:
venv\Scripts\activate

3. Установить зависимости:
pip install -r requirements.txt

4. Настроить PostgreSQL в файле settings.py

5. Выполнить миграции:
python manage.py migrate

6. Создать суперпользователя:
python manage.py createsuperuser

7. Запустить сервер:
python manage.py runserver

---

## Используемые технологии

- Python
- Django
- Django REST Framework
- PostgreSQL
- psycopg2-binary
- drf-spectacular
- JWT (SimpleJWT)