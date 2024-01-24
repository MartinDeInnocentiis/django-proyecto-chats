from django.urls import path

# Importamos las API_VIEWS:
from canales.api.views import *


urlpatterns = [
    path('canales/chats/', GetChatsAPIView.as_view(), name='chat-list-create'),
    path('canales/chats/<int:pk>/', ChatRetrieveUpdateAPIView.as_view(), name='chat-retrieve-update'),
    path('canales/mensajes/', MensajeGetCreateAPIView.as_view(), name='mensaje-get-create'),
    path('chats/<int:chat_id>/mensajes/', ChatMensajesListView.as_view(), name='chat-mensajes-list'),
    path('chats/<int:chat_id>/mensajes/<str:username>/', ChatUserMensajesListView.as_view(), name='chat-user-mensajes'),
    ]