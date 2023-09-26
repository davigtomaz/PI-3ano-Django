from rest_framework.serializers import ModelSerializer
from livraria.models import Devolucao

class DevolucaoSerializer(ModelSerializer):
    class Meta:
        model = Devolucao
        fields = "__all__"