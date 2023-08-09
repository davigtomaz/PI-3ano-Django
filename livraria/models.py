from django.db import models
from uploader.models import Image

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    categoria = models.ManyToManyField(Categoria,  related_name='livros')
    editora = models.ManyToManyField(Editora,  related_name='livros')
    autores = models.ManyToManyField(Autor,  related_name='livros')
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
        