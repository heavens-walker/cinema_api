from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Hall, Session, Booking
from .serializers import MovieSerializer, HallSerializer, SessionSerializer, BookingSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API для работы с фильмами
    
    Список действий:
    - GET /api/v1/movies/ - получить список всех фильмов
    - GET /api/v1/movies/{id}/ - получить конкретный фильм
    - POST /api/v1/movies/ - создать фильм или группу фильмов
    - PUT /api/v1/movies/{id}/ - обновить фильм
    - PATCH /api/v1/movies/{id}/ - частично обновить фильм
    - DELETE /api/v1/movies/{id}/ - удалить фильм
    - DELETE /api/v1/movies/batch/?ids=1,2,3 - удалить несколько фильмов
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.query_params.get('title')
        director = self.request.query_params.get('director')
        if title:
            qs = qs.filter(title__icontains=title)
        if director:
            qs = qs.filter(director__icontains=director)
        return qs

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [Movie.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [Movie.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=400)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=204)


class HallViewSet(viewsets.ModelViewSet):
    """API для работы с фильмами
    Список действий:
    - GET /api/v1/movies/ - получить список всех фильмов
    - GET /api/v1/movies/{id}/ - получить конкретный фильм
    - POST /api/v1/movies/ - создать фильм или группу фильмов
    - PUT /api/v1/movies/{id}/ - обновить фильм
    - PATCH /api/v1/movies/{id}/ - частично обновить фильм
    - DELETE /api/v1/movies/{id}/ - удалить фильм
    - DELETE /api/v1/movies/batch/?ids=1,2,3 - удалить несколько фильмов
    """
    serializer_class = HallSerializer
    queryset = Hall.objects.all()

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [Hall.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [Hall.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=400)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=204)


class SessionViewSet(viewsets.ModelViewSet):
    """API для работы с фильмами
    Список действий:
    - GET /api/v1/movies/ - получить список всех фильмов
    - GET /api/v1/movies/{id}/ - получить конкретный фильм
    - POST /api/v1/movies/ - создать фильм или группу фильмов
    - PUT /api/v1/movies/{id}/ - обновить фильм
    - PATCH /api/v1/movies/{id}/ - частично обновить фильм
    - DELETE /api/v1/movies/{id}/ - удалить фильм
    - DELETE /api/v1/movies/batch/?ids=1,2,3 - удалить несколько фильмов
    """
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        movie_id = self.request.query_params.get('movie_id')
        hall_id = self.request.query_params.get('hall_id')
        if movie_id:
            qs = qs.filter(movie_id=movie_id)
        if hall_id:
            qs = qs.filter(hall_id=hall_id)
        return qs

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [Session.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [Session.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=400)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=204)


class BookingViewSet(viewsets.ModelViewSet):
    """API для работы с фильмами
    Список действий:
    - GET /api/v1/movies/ - получить список всех фильмов
    - GET /api/v1/movies/{id}/ - получить конкретный фильм
    - POST /api/v1/movies/ - создать фильм или группу фильмов
    - PUT /api/v1/movies/{id}/ - обновить фильм
    - PATCH /api/v1/movies/{id}/ - частично обновить фильм
    - DELETE /api/v1/movies/{id}/ - удалить фильм
    - DELETE /api/v1/movies/batch/?ids=1,2,3 - удалить несколько фильмов
    """
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        session_id = self.request.query_params.get('session_id')
        if session_id:
            qs = qs.filter(session_id=session_id)
        return qs

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [Booking.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            instances = [Booking.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'], url_path='batch')
    def batch_delete(self, request):
        ids = request.query_params.get('ids')
        if not ids:
            return Response({'error': 'ids parameter required'}, status=400)
        ids_list = [int(pk) for pk in ids.split(',')]
        self.queryset.filter(pk__in=ids_list).delete()
        return Response(status=204)