from django.db import models
from livraria.models.livro import Livro
class Emprestimo(models.Model):
    nome_livro = models.ForeignKey(Livro, on_delete=models.PROTECT ,related_name='emprestimos', blank=True, null=True)
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    inicio = models.DateField(max_length=255)
    final = models.DateField(max_length=255)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = "Empréstimos"