from django.db import models



class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    categoria = models.CharField(max_length=32, null=True, blank=True)
    editora = models.CharField(max_length=32, null=True, blank=True)
    autores = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.titulo