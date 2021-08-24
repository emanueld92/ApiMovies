from django.contrib.auth import authenticate,login,logout
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
# Create your views here.

class LoginView(APIView):
    def post(self, request):
        #Recuperar las credenciales y autenticamos al usuario
        email=request.data.get('email',None)
        password=request.data.get('password', None)
        user=authenticate(email=email, password=password)
        
        #si la validaicon es correcta agreagamos a request la informacion de sesion
        if user:
            login(request,user)
            return Response(UserSerializer(user).data,status=status.HTTP_200_OK)
        
        #si no es correcto devolvemos un error en la peticion
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class LogoutView(APIView):
    def post(self , request):
        #borrar de request la informacion de session
        logout(request)
        
        #Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK,)
#Crear nuevo usuario    
class signupView(generics.CreateAPIView):
    serializer_class=UserSerializer

#funcion para cambiar password mediante validacion token de correo electronico
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    #Envio de correo al cliente para recuperacion de password
 print(
     f"\nRecupera la contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API http://localhost:8000/api/auth/reset/confirm/.")
