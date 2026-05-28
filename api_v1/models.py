from django.db import models
from django.conf import settings

class Movie(models.Model):
    """Модель фильма"""
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    duration = models.IntegerField(help_text="Длительность в минутах", verbose_name="Длительность")
    release_date = models.DateField(null=True, blank=True, verbose_name="Дата выхода")
    director = models.CharField(max_length=255, blank=True, verbose_name="Режиссёр")
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['-created_at']


class Hall(models.Model):
    """Модель зала кинотеатра"""
    name = models.CharField(max_length=100, verbose_name="Название зала")
    capacity = models.IntegerField(help_text="Количество мест", verbose_name="Вместимость")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"


class Session(models.Model):
    """Модель киносеанса"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions', verbose_name="Фильм")
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='sessions', verbose_name="Зал")
    start_time = models.DateTimeField(verbose_name="Время начала")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена билета")
    available_seats = models.IntegerField(verbose_name="Доступно мест")

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"
        ordering = ['start_time']


class Booking(models.Model):
    """Модель бронирования билета"""
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='bookings', verbose_name="Сеанс")
    customer_name = models.CharField(max_length=255, verbose_name="Имя клиента")
    customer_email = models.EmailField(verbose_name="Email клиента")
    seats_count = models.IntegerField(verbose_name="Количество мест")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата бронирования")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='bookings',
        verbose_name="Пользователь"
    )

    def __str__(self):
        return f"Бронирование {self.customer_name} на {self.session}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
        ordering = ['-created_at']