import uuid
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Film(models.Model):
    def path_to_film( instance, filename):
        return f'films/{instance.id}/{filename}'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("title", max_length=150)
    year = models.PositiveIntegerField("year", default=2000)
    review_short = models.TextField("Argument", null=True, blank=True)
    review_large = models.TextField("Argument Large", blank=True)
    trailer_url = models.URLField(
        "URL youtube", max_length=200, blank=True, null=True)
    genres = models.ManyToManyField('FilmGenre', related_name="film_genres",
                                    verbose_name="Genres")

    image_thumbnail = models.ImageField(
        upload_to=path_to_film, null=True, blank=True, verbose_name="Miniatura")
    image_wallpaper = models.ImageField(
        upload_to=path_to_film, null=True, blank=True, verbose_name="Wallpaper")

    class Meta:
        verbose_name = "Película"
        ordering = ['title']

    def __str__(self):
        return f'{self.title} ({self.year})'


class FilmGenre(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Nombre", unique=True)
    slug = models.SlugField(
        unique=True)

    class Meta:
        verbose_name = "género"
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(FilmGenre, self).save(*args, **kwargs)
