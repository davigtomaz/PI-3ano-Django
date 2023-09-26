from rest_framework.viewsets import ModelViewSet

from livraria.models import Devolucao
from livraria.serializers import DevolucaoSerializer


class DevolucaoViewSet(ModelViewSet):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer