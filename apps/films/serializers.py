from rest_framework import serializers
from .models import *

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Film
        fields='__all__'
        
    class NestedFilmGenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = FilmGenre
            fields = '__all__'

    genres = NestedFilmGenreSerializer(many=True)
        
class FilmGenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = FilmGenre
        fields='__all__'
        
    class NestedFilmSerializer(serializers.ModelSerializer):
        class Meta:
            model=Film
            fields=['id','title','image_thumbnail']
            
        
    films= NestedFilmSerializer(many=True, read_only=True)
