from django. db import models

class Emprestimo(models.Model):
    nome = models.CharField(max_length=255)
    dia = models.DateField(max_length=255)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Empréstimos"