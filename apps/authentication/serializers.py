from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)
    avatar= serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password','avatar')

    def validate_password(self,value):
        return make_password(value)
    
    def update(self, instance, validated_data):
        validated_data.pop('email',None) #previene la edicion del correo
        return super().update(instance, validated_data)
    
    def validate_password(self, value):
        return make_password(value)
    
    def validate_username(self,value):
        value=value.replace(" ","")
        try:
            user=get_user_model().objects.get(username=value)
            if user==self.instance:
                return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError('Nombre de Usuario en Uso, intente con otro')
        
    def validate_email(self,value):
        #Comprobar que no exista otro usuario con el mismo email 
        try:
            user = get_user_model().objects.get(email=value)
        except get_user_model().DoesNotExist:
            return value
        #si no fallara la validacion
        raise serializers.ValidationError('Email  en uso')