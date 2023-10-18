from rest_framework.serializers import ModelSerializer
from livraria.models import Localização

class LocalizaçãoSerializer(ModelSerializer):
    class Meta:
        model = Localização
        fields = "__all__"