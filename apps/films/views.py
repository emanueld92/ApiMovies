from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, status, views, authentication, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


class ExtendedPagination(PageNumberPagination):
    page_size = 8

    def get_paginated_response(self, data):
        next_link = self.get_next_link()
        previous_link = self.get_previous_link()

        if next_link:
            # el -1 nos devulve el ultimo elmento de la cadena resultatne del split
            next_link = next_link.split('/')[-1]

        if previous_link:
            previous_link = previous_link.split('/')[-1]

        return Response({
            'count': self.page.paginator.count,  # Cuenta el numero de paginas
            # numero de pagina en el cual estamos
            'num_pages': self.page.paginator.num_pages,
            'page_size': self.page_size,
            'next_link': next_link,  # Pagina siguiente
            'previus_link': previous_link,
            'results': data
        })


class FilmVieSet(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    # Sistema de filtros
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    # campos por los cuales se hace la busqueda, se pasan en forma de lista
    search_fields = ['title', 'year', 'genres_name']

    # compos para ordenar busqueda
    ordering_fields = ['title', 'year',
                       'genres__name', 'favorites', 'average_note']
    filterset_fields = {
        'year': ['lte', 'gte'],  # por año menor o mayor
        'genres': ['exact']   # por genero exacto
    }

    # Sistema de Paginacion

    pagination_class = ExtendedPagination


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FilmGenre.objects.all()
    serializer_class = FilmGenreSerializers
    lookup_field = 'Slug'  # indentificacion de genero usando slug


class FilmUserViewSet(views.APIView):
    authentication_classes = [authentication.SessionAuthentication]  #validacion para que el usuario este autenticado
    permission_classes = [permissions.IsAuthenticated]  

    # El método GET devolverá las peliculas del usuario
    def get(self, request, *args, **kwargs):
        queryset = FilmUser.objects.filter(user=self.request.user)
        serializer = FilmUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # El método POST permitirá gestionar su información de la película
    def post(self, request, *args, **kwargs):
        try:
            film = Film.objects.get(id=request.data['uuid'])
        except Film.DoesNotExist:
            return Response(
                {'status': 'Film not found'},
                status=status.HTTP_404_NOT_FOUND)

        # Una vez recuperada la película creamos o recuperamos su FilmUser
        film_user, created = FilmUser.objects.get_or_create(
            user=request.user, film=film)

        # Configuramos cada campo
        film_user.state = request.data.get('state', 0)
        film_user.favorite = request.data.get('favorite', False)
        film_user.note = request.data.get('note', -1)
        film_user.review = request.data.get('review', None)

        # Si se marca la pelicula como NO VISTA la borramos automáticamente
        if int(film_user.state) == 0:
            film_user.delete()
            return Response(
                {'status': 'Deleted'}, status=status.HTTP_200_OK)

        # En otro caso guardamos los campos de la película de usuario
        else:
            film_user.save()

        return Response(
            {'status': 'Saved'}, status=status.HTTP_200_OK)
