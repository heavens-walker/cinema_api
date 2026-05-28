from django.contrib import admin
from .models import Movie, Hall, Session, Booking


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'director', 'duration', 'rating', 'release_date']
    search_fields = ['title', 'director']


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'hall', 'start_time', 'price', 'available_seats']
    list_filter = ['movie', 'hall']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'session', 'customer_name', 'customer_email', 'seats_count', 'created_at']
    search_fields = ['customer_name', 'customer_email']