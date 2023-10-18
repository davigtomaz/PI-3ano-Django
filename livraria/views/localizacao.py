from rest_framework.viewsets import ModelViewSet

from livraria.models import Localização
from livraria.serializers import LocalizaçãoSerializer


class LocalizaçãoViewSet(ModelViewSet):
    queryset = Localização.objects.all()
    serializer_class = LocalizaçãoSerializer