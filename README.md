# Cinema API

Учебный проект по дисциплине 
«Инструментальные средства разработки ПО».

## Описание

REST API для управления кинотеатром.
Позволяет работать с фильмами, актёрами и сеансами.

Проект реализован на Django и Django REST Framework.

## Функциональность

- Получение списка фильмов, актёров и сеансов
- Получение одного объекта по id
- Создание объектов
- Обновление (PATCH)
- Удаление
- Фильтрация фильмов по названию
- Фильтрация сеансов по фильму
- JWT-авторизация
- Swagger документация

## Эндпоинты

### Актёры
GET /api/v1/actors/  
GET /api/v1/actors/{id}/  
POST /api/v1/actors/  
PATCH /api/v1/actors/{id}/  
DELETE /api/v1/actors/{id}/  

### Фильмы
GET /api/v1/movies/  
GET /api/v1/movies/{id}/  
POST /api/v1/movies/  
PATCH /api/v1/movies/{id}/  
DELETE /api/v1/movies/{id}/  

Фильтрация:
GET /api/v1/movies/?title=название

### Сеансы
GET /api/v1/sessions/  
GET /api/v1/sessions/{id}/  
POST /api/v1/sessions/  
PATCH /api/v1/sessions/{id}/  
DELETE /api/v1/sessions/{id}/  

Фильтрация:
GET /api/v1/sessions/?movie_id=1

## Документация API

/api/schema/swagger-ui/

## Запуск проекта

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

## Используемые технологии

Python  
Django  
Django REST Framework  
drf-spectacular  
JWT (SimpleJWT)
