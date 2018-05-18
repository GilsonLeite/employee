from rest_framework.viewsets import ModelViewSet
from cadastro.models import Cadastro
from . serializer import CadastroSerializer 

class CadastroViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
