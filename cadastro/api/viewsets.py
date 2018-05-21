from rest_framework.viewsets import ModelViewSet
from cadastro.models import Cadastro
from . serializer import CadastroSerializer


class CadastroViewSet(ModelViewSet):

    serializer_class = CadastroSerializer

    def get_queryset(self):
        return Cadastro.objects.filter(active=True)
