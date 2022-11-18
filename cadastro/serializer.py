from rest_framework import serializers
from cadastro.models import Usuario

class UsuarioSeralizer(serializers.ModelSerializer):
    class Meta: 
        model = Usuario
        fields = ['id', 'login', 'senha', 'data_nascimento']
