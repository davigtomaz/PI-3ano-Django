from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Livro

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ["id", "titulo", "isbn", "categoria", "editora", "autores"]