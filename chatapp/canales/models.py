from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class Chat(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(max_length=60, default='', verbose_name='name')
    
    class Meta:
        db_table = 'canales_chats'
        verbose_name = 'chat'
        verbose_name_plural = 'chats'
        
    def __str__ (self):
        return f'{self.id} - {self.nombre}'
    
    
class Mensaje (models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE, related_name='mensajes')
    chat = models.ForeignKey(Chat, verbose_name='chat', on_delete=models.CASCADE, related_name='mensajes')
    contenido = models.CharField(verbose_name='content', max_length=300, default='')
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        db_table = 'canales_msj'
        verbose_name = 'mensaje'
        verbose_name_plural = 'mensajes'
        
    def __str__ (self):
        return f'{self.id} - {self.user} - {self.chat} - {self.creado} - {self.contenido}'