from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = "Autores"