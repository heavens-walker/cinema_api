# Cinema API

Учебный проект по дисциплине  
«Инструментальные средства разработки программного обеспечения».

## Описание

Cinema API — это REST API для управления кинотеатром.  
Реализована работа с фильмами, залами, сеансами и бронированиями билетов.

Проект разработан с использованием Django и Django REST Framework.  
В качестве базы данных используется PostgreSQL.

---

## Реализованный функционал

- Получение списка объектов
- Получение одного объекта по ID
- Создание одного объекта
- Массовое создание (списком)
- Полное обновление (PUT)
- Частичное обновление (PATCH)
- Удаление одного объекта
- Массовое удаление через параметр `ids`
- Фильтрация данных через query-параметры
- JWT‑авторизация
- Swagger-документация

---

## Эндпоинты API

### Фильмы (/api/v1/movies/)

- GET /api/v1/movies/ — список фильмов  
- GET /api/v1/movies/{id}/ — детали фильма  
- GET /api/v1/movies/?title=название — фильтрация по названию  
- GET /api/v1/movies/?director=режиссер — фильтрация по режиссеру  
- POST /api/v1/movies/ — создание фильма или списка фильмов  
- PUT /api/v1/movies/{id}/ — полное обновление  
- PATCH /api/v1/movies/{id}/ — частичное обновление  
- DELETE /api/v1/movies/{id}/ — удаление  
- DELETE /api/v1/movies/batch/?ids=1,2,3 — массовое удаление  

---

### Залы (/api/v1/halls/)

- GET /api/v1/halls/ — список залов  
- GET /api/v1/halls/{id}/ — детали зала  
- POST /api/v1/halls/ — создание одного или нескольких залов  
- PUT /api/v1/halls/{id}/ — полное обновление  
- PATCH /api/v1/halls/{id}/ — частичное обновление  
- DELETE /api/v1/halls/{id}/ — удаление  
- DELETE /api/v1/halls/batch/?ids=1,2,3 — массовое удаление  

---

### Сеансы (/api/v1/sessions/)

- GET /api/v1/sessions/ — список сеансов  
- GET /api/v1/sessions/{id}/ — детали сеанса  
- GET /api/v1/sessions/?movie_id=1 — фильтрация по фильму  
- GET /api/v1/sessions/?hall_id=1 — фильтрация по залу  
- POST /api/v1/sessions/ — создание одного или нескольких сеансов  
- PUT /api/v1/sessions/{id}/ — полное обновление  
- PATCH /api/v1/sessions/{id}/ — частичное обновление  
- DELETE /api/v1/sessions/{id}/ — удаление  
- DELETE /api/v1/sessions/batch/?ids=1,2,3 — массовое удаление  

---

### Бронирования (/api/v1/bookings/)

- GET /api/v1/bookings/ — список бронирований  
- GET /api/v1/bookings/{id}/ — детали бронирования  
- GET /api/v1/bookings/?session_id=1 — фильтрация по сеансу  
- POST /api/v1/bookings/ — создание одного или нескольких бронирований  
- PUT /api/v1/bookings/{id}/ — полное обновление  
- PATCH /api/v1/bookings/{id}/ — частичное обновление  
- DELETE /api/v1/bookings/{id}/ — удаление  
- DELETE /api/v1/bookings/batch/?ids=1,2,3 — массовое удаление  

---

## Документация API

Swagger UI доступен по адресу:
http://127.0.0.1:8000/api/schema/swagger-ui/

---

## Установка и запуск проекта

1. Клонировать репозиторий

2. Создать виртуальное окружение:
python -m venv venv

3. Активировать окружение:
venv\Scripts\activate

4. Установить зависимости:
pip install -r requirements.txt


5. Настроить подключение к PostgreSQL в файле settings.py

6. Выполнить миграции:
python manage.py migrate


7. Создать суперпользователя:
python manage.py createsuperuser

8. Запустить сервер:
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