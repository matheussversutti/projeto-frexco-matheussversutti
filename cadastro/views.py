from rest_framework import viewsets
from cadastro.models import Usuario
from cadastro.serializer import UsuarioSeralizer


class UsuariosViewSet(viewsets.ModelViewSet):
    #Vai me mostrar todos os usuarios cadastrados
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSeralizer