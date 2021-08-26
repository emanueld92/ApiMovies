from django.contrib.auth.models import AbstractUser
from django.db import models


def path_avatar(instance, filename):
    return f'avatars/{instance.id}/{filename}'


class CustomUser(AbstractUser):

    email = models.EmailField(
        max_length=150, unique=True)
    USERNAME_FIELD = 'email'  # new
    REQUIRED_FIELDS = ['username', 'password']  # new
    avatar = models.ImageField(
        'Avatar', upload_to=path_avatar, null=True, blank=True)
