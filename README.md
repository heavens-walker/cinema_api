# Cinema API

API для управления кинотеатром с использованием Django REST Framework.

## Функционал

- Управление фильмами (Movie)
- Управление залами (Hall)
- Управление сеансами (Session)
- Управление бронированиями билетов (Booking)

## Эндпоинты

### Фильмы (/api/v1/movies/)
- `GET /api/v1/movies/` - список всех фильмов
- `GET /api/v1/movies/{id}/` - детали фильма
- `GET /api/v1/movies/?title=название` - фильтр по названию
- `GET /api/v1/movies/?director=режиссер` - фильтр по режиссеру
- `POST /api/v1/movies/` - создание фильма или списка фильмов
- `PUT /api/v1/movies/{id}/` - полное обновление фильма
- `PATCH /api/v1/movies/{id}/` - частичное обновление фильма
- `DELETE /api/v1/movies/{id}/` - удаление фильма
- `DELETE /api/v1/movies/batch/?ids=1,2,3` - массовое удаление

### Залы (/api/v1/halls/)
- `GET /api/v1/halls/` - список залов
- `GET /api/v1/halls/{id}/` - детали зала
- `POST /api/v1/halls/` - создание зала или списка залов
- `PUT /api/v1/halls/{id}/` - обновление зала
- `PATCH /api/v1/halls/{id}/` - частичное обновление зала
- `DELETE /api/v1/halls/{id}/` - удаление зала
- `DELETE /api/v1/halls/batch/?ids=1,2,3` - массовое удаление

### Сеансы (/api/v1/sessions/)
- `GET /api/v1/sessions/` - список сеансов
- `GET /api/v1/sessions/{id}/` - детали сеанса
- `GET /api/v1/sessions/?movie_id=1` - фильтр по фильму
- `GET /api/v1/sessions/?hall_id=1` - фильтр по залу
- `POST /api/v1/sessions/` - создание сеанса или списка сеансов
- `PUT /api/v1/sessions/{id}/` - обновление сеанса
- `PATCH /api/v1/sessions/{id}/` - частичное обновление сеанса
- `DELETE /api/v1/sessions/{id}/` - удаление сеанса
- `DELETE /api/v1/sessions/batch/?ids=1,2,3` - массовое удаление

### Бронирования (/api/v1/bookings/)
- `GET /api/v1/bookings/` - список бронирований
- `GET /api/v1/bookings/{id}/` - детали бронирования
- `GET /api/v1/bookings/?session_id=1` - фильтр по сеансу
- `POST /api/v1/bookings/` - создание бронирования или списка бронирований
- `PUT /api/v1/bookings/{id}/` - обновление бронирования
- `PATCH /api/v1/bookings/{id}/` - частичное обновление бронирования
- `DELETE /api/v1/bookings/{id}/` - удаление бронирования
- `DELETE /api/v1/bookings/batch/?ids=1,2,3` - массовое удаление

## Установка и запуск

1. Клонировать репозиторий
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать: `venv\Scripts\activate` (Windows) или `source venv/bin/activate` (Mac/Linux)
4. Установить зависимости: `pip install -r requirements.txt`
5. Выполнить миграции: `python manage.py migrate`
6. Создать суперпользователя: `python manage.py createsuperuser`
7. Запустить сервер: `python manage.py runserver`

## Документация

Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/

