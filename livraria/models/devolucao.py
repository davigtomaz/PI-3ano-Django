from django. db import models

class Devolucao(models.Model):
    nome = models.CharField(max_length=255)
    dia = models.DateField(max_length=255)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Devoluções"