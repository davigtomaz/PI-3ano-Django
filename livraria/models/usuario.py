from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return self.nome