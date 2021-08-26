from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

class ExtendedPagination(PageNumberPagination):
    page_size=8
    
    def get_paginated_response(self, data):
        next_link=self.get_next_link()
        previous_link=self.get_previous_link()
        
        if next_link:
            next_link= next_link.split('/')[-1] #el -1 nos devulve el ultimo elmento de la cadena resultatne del split
            
            
        if previous_link:
            previous_link=previous_link.split('/')[-1]
        
        return Response({
            'count': self.page.paginator.count, #Cuenta el numero de paginas
            'num_pages': self.page.paginator.num_pages,#numero de pagina en el cual estamos
            'page_size':self.page_size,
            'next_link':next_link,#Pagina siguiente
            'previus_link':previous_link,
            'results':data
        })

class FilmVieSet(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    # Sistema de filtros
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    # campos por los cuales se hace la busqueda, se pasan en forma de lista
    search_fields = ['title', 'year', 'genres_name']

    # compos para ordenar busqueda
    ordering_fields = ['title', 'year', 'genres_name']
    filterset_fields = {
        'year': ['lte', 'gte'],  # por año menor o mayor
        'genres': ['exact']   # por genero exacto
    }
    
    ##Sistema de Paginacion
    
    pagination_class= ExtendedPagination
   

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FilmGenre.objects.all()
    serializer_class = FilmGenreSerializers
    lookup_field = 'Slug'  # indentificacion de genero usando slug
