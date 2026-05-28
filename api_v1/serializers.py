from rest_framework import serializers
from .models import Movie, Hall, Session, Booking


class MovieSerializer(serializers.ModelSerializer):
    """Сериализатор для фильмов"""
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'release_date', 
                  'director', 'rating', 'created_at']
        
    def to_representation(self, instance):
        """Переводим названия полей на русский для вывода"""
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'название': data['title'],
            'описание': data['description'],
            'длительность_минуты': data['duration'],
            'дата_выхода': data['release_date'],
            'режиссёр': data['director'],
            'рейтинг': data['rating'],
            'создано': data['created_at'],
        }


class HallSerializer(serializers.ModelSerializer):
    """Сериализатор для залов"""
    
    class Meta:
        model = Hall
        fields = ['id', 'name', 'capacity']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'название': data['name'],
            'вместимость': data['capacity'],
        }


class SessionSerializer(serializers.ModelSerializer):
    """Сериализатор для сеансов"""
    movie = MovieSerializer(read_only=True)
    hall = HallSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source='movie', write_only=True
    )
    hall_id = serializers.PrimaryKeyRelatedField(
        queryset=Hall.objects.all(), source='hall', write_only=True
    )

    class Meta:
        model = Session
        fields = ['id', 'movie', 'movie_id', 'hall', 'hall_id', 
                  'start_time', 'price', 'available_seats']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'фильм': data['movie'],
            'зал': data['hall'],
            'время_начала': data['start_time'],
            'цена': data['price'],
            'доступно_мест': data['available_seats'],
        }


class BookingSerializer(serializers.ModelSerializer):
    """Сериализатор для бронирований"""
    session = serializers.StringRelatedField(read_only=True)
    session_id = serializers.PrimaryKeyRelatedField(
        queryset=Session.objects.all(), source='session', write_only=True
    )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'session', 'session_id', 'customer_name', 
                  'customer_email', 'seats_count', 'user', 'created_at']
        read_only_fields = ['user']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'сеанс': data['session'],
            'имя_клиента': data['customer_name'],
            'email_клиента': data['customer_email'],
            'количество_мест': data['seats_count'],
            'пользователь': data.get('user'),
            'создано': data['created_at'],
        }