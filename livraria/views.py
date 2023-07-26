from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Livro
from livraria.serializers import CategoriaSerializer, LivroDetailSerializer, LivroSerializer, LivroListSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer