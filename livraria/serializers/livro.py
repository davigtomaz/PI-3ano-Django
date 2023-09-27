from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, SerializerMethodField

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
    # capa = ImageSerializer(required=False)
    capa = CharField(source="capa.url")
    class Meta:
        model = Livro
        fields = ("id", "titulo", "categoria", "editora", "capa")

class LivroListSerializer(ModelSerializer):
    capa = CharField(source="capa.url")
    # categoria = CategoriaItem(many=True)
    categoria = SerializerMethodField()
    class Meta:
        model = Livro
        fields = ["id", "titulo", "categoria", "editora", "autores", "capa"]

    def get_categoria(self, obj):
        return [categoria.nome for categoria in obj.categoria.all()]