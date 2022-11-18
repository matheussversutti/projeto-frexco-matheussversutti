from django.contrib import admin
from cadastro.models import Usuario
# Register your models here.

class Usuarios(admin.ModelAdmin): 
    list_display = ('id', 'login', 'senha', 'data_nascimento')
    list_display_links = ('id', 'login', 'senha')
    search_fields = ('login',)

admin.site.register(Usuario, Usuarios)