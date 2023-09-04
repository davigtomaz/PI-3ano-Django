from django.db import models
from uploader.models import Image
from livraria.models import Autor, Categoria, Editora, Localização


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.DecimalField(decimal_places=0, max_digits=13)
    categoria = models.ManyToManyField(Categoria,  related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT ,related_name='livros')
    autores = models.ManyToManyField(Autor,  related_name='livros')
    localizacao = models.ForeignKey(Localização, on_delete=models.PROTECT, related_name='livros')
    emprestimo = models.DateField(null=True, blank=True)
    devolucao = models.DateField(null=True, blank=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.titulo