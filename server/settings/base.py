"""
Django settings for server project.

Using Django 3.2.6.


"""

from pathlib import Path
from django.apps import AppConfig
import os

AppConfig.default = False
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = []


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


]

LOCAL_APPS = [
    'apps.authentication',
    'apps.films',

]
THIRD_APPS = [
    'corsheaders',
    'rest_framework',
    'django_rest_passwordreset',
    'django_filters',
    'drf_spectacular',
    
]

INSTALLED_APPS = BASE_APPS+LOCAL_APPS+THIRD_APPS
AUTH_USER_MODEL = "authentication.CustomUser"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True


USE_TZ = True


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Agregamos las urls que puedan hacerle peticiones de tipo Cors a django, en este caso React
CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]
CORS_ALLOW_CREDENTIALS = True

#configuration media root for manage to file
MEDIA_ROOT=os.path.join(BASE_DIR, 'media') #path to server local
MEDIA_URL = 'http://localhost:8000/media/' #URL for developer


##Spectacular api doc
REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Movies Api',
    'DESCRIPTION': 'Api Movies api with ReactJs',
    'VERSION': '1.0.0',
    
}
