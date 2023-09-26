from rest_framework.viewsets import ModelViewSet

from livraria.models import Emprestimo
from livraria.serializers import EmprestimoSerializer


class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer