from django.urls import path, include
from .views import *
urlpatterns = [
    # Auth vies
    # Login endPoint
    path('auth/login', LoginView.as_view(), name='login'),

    # Logout EndPoint
    path('auth/logout', LogoutView.as_view(), name='logout'),
    # Signup Endpoint
    path('auth/signup/', signupView.as_view(), name='signup'),

    # ResetPasswor Endpoint
    path('auth/reset/', include('django_rest_passwordreset.urls',
         namespace='password_reset')),
    
    #Modificar perfiles de usuario
    path('user/profile/',ProfileView.as_view(), name='user_profile'),
]
