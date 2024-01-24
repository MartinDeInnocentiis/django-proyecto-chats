from django.contrib.auth import authenticate
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
# (GET - ListAPIView) Listar todos los elementos en la entidad:
# (POST - CreateAPIView) Inserta elementos en la DB
# (GET - RetrieveAPIView) Devuelve un solo elemento de la entidad.
# (GET-POST - ListCreateAPIView) Para listar o insertar elementos en la DB
# (GET-PUT - RetrieveUpdateAPIView) Devuelve o actualiza un elemento en particular.
# (DELETE - DestroyAPIView) Permite eliminar un elemento.
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    GenericAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django.db.models import Q
# NOTE: Importamos este decorador para poder customizar los 
# parámetros y responses en Swagger, para aquellas
# vistas de API basadas en funciones y basadas en Clases 
# que no tengan definido por defecto los métodos HTTP.
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from canales.api.serializers import *
from canales.models import *
from rest_framework.pagination import PageNumberPagination


class MensajePagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 100

class GetChatsAPIView(ListCreateAPIView):
    queryset = Chat.objects.all().order_by('id')
    serializer_class = ChatSerializer
    
    
class ChatRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
class MensajeGetCreateAPIView(ListCreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    pagination_class = MensajePagination

    def post(self, request, *args, **kwargs):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChatMensajesListView(ListAPIView):
    serializer_class = MensajeSerializer
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return Mensaje.objects.filter(chat_id=chat_id)
    
    
class ChatUserMensajesListView(ListAPIView):
    serializer_class = MensajeSerializer

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        return Mensaje.objects.filter(chat_id=chat_id, user=user)