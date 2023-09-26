from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from livraria.models import Livro
from uploader.models import Image
from uploader.serializers import ImageSerializer

class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    

    class Meta:
        model = Livro
        fields = ("id", "titulo", "categoria", "editora", "capa", "capa_attachment_key")

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ("id", "titulo", "categoria", "editora" "capa", "capa_attachment_key")
    # capa = ImageSerializer(required=False)
    capa = CharField(source="capa.url")

class LivroListSerializer(ModelSerializer):
    capa = CharField(source="capa.url")
    class Meta:
        model = Livro
        fields = ["id", "titulo", "categoria", "editora", "autores", "capa"]