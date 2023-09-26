from rest_framework.serializers import ModelSerializer
from livraria.models import Emprestimo

class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = "__all__"