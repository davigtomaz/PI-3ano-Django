from rest_framework.serializers import ModelSerializer, SlugRelatedField

from livraria.models import Categoria
from uploader.models import Image

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"