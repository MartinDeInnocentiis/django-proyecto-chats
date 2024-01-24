from django.contrib import admin

from canales.models import *

# Register your models here.


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
 
    list_filter= ('id','nombre')
    

@admin.register(Mensaje)
class wish_listAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'chat', 'contenido', 'creado')
    list_filter= ('id','user', 'chat', 'contenido', 'creado')
