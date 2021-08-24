from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass

@admin.register(FilmGenre)
class FilmGenreAdmin (admin.ModelAdmin):
    readonly_fields=['slug']

