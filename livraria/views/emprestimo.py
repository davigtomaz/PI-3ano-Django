from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Emprestimo
from livraria.serializers import EmprestimoDetailSerializer, EmprestimoSerializer, EmprestimoListSerializer

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return EmprestimoListSerializer
        elif self.action == "retrieve":
            return EmprestimoDetailSerializer
        return EmprestimoSerializer