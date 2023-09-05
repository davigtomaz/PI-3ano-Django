from django.db import models

from usuario.models import Usuario
from livraria.models import Livro

class Carrinho(models.Model):
    class StatusCarrinho(models.IntegerChoices):
        ESTANTE = (1,"Estante",)
        EMPRESTADO = (2,"Emprestado",)
        PERDIDO = (3,"Perdio",)
        DEVOLVIDO = (4,"Devolvido",)

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="carrinhos")
    status = models.IntegerField(choices=StatusCarrinho.choices,  default=StatusCarrinho.ESTANTE)

class ItensCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)