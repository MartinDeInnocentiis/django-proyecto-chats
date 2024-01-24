from django.contrib.auth.models import User

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from canales.models import Chat, Mensaje


class ChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Chat
        fields = ('id','nombre',)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ('password',)
        
        
class MensajeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    chat = serializers.PrimaryKeyRelatedField(
        queryset=Chat.objects.all()
    )

    class Meta:
        model = Mensaje
        fields = ('id', 'user', 'chat', 'contenido', 'creado')