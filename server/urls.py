"""server URL Configuration

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from apps.films import views as film_views
#Routers APi
routers=routers.DefaultRouter()
routers.register('films', film_views.FilmVieSet, basename='Film')
routers.register('genres', film_views.GenreViewSet, basename='FilmGenre')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #
    path('api/', include('apps.authentication.urls')),
    path('api/', include(routers.urls)),
    
    #vista de peliculas favoritas por usuario
    path('api/userfilms/', film_views.FilmUserViewSet.as_view())
]


if settings.DEBUG:
    urlpatterns+=static('/media/', document_root=settings.MEDIA_ROOT)
