from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField, DateField
from livraria.models import Emprestimo, Livro
from django.db import models

class EmprestimoSerializer(ModelSerializer):
     
    class Meta:
        model = Emprestimo
        fields = ("id", "nome", "contato", "inicio", "final","nome_livro")
        depth = 2
        
class EmprestimoDetailSerializer(ModelSerializer):

    class Meta:
        model = Emprestimo
        fields = ("id", "nome", "contato", "inicio", "final","nome_livro")
        depth = 2

class EmprestimoListSerializer(ModelSerializer):
    nome_livro = models.ForeignKey(Livro, on_delete=models.PROTECT ,related_name='emprestimos', blank=True, null=True)
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    inicio = models.DateField(max_length=255)
    final = models.DateField(max_length=255)
    class Meta:
        model = Emprestimo
        fields = ["id", "nome", "contato", "inicio", "final","nome_livro"]
        depth = 2
