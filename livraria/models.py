from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.CharField(max_length=32, null=True, blank=True)
    autores = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.titulo
        