# from django.db import models
# from uploader.models import Image

# class Categoria(models.Model):
#     nome = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nome

# class Editora(models.Model):
#     nome = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nome

# class Autor(models.Model):
#     nome = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nome

# class Localização(models.Model):
#     nome = models.CharField(max_length=255)

#     def __str__(self):
#         return self.nome

# # class Cliente(models.Model):
# #     nome = models.CharField(max_length=255)
# #     email = models.EmailField(max_length=255)
# #     senha = models.CharField(max_length=255, null=True, blank=True, default=None)
# #     feedback = models.CharField(max_length=255,null=True, blank=True, default=None)
# #     relatorio = models.CharField(max_length=255, null=True, blank=True, default=None)

# #     def __str__(self):
# #         return self.nome
# #  O CLIENTE DEVE SER CRIADO NA PARTE DO DJANGO ADMIN COMO FOI FEITO NO TUTORIAL DO PROF EM QUE REGISTRAMOS COMPRADOR E ADMINISTRADOR


# class Usuario(models.Model):
#     nome = models.CharField(max_length=255)
#     telefone = models.DecimalField(max_digits=11, decimal_places=0)

#     def __str__(self):
#         return self.nome


# class Livro(models.Model):
#     titulo = models.CharField(max_length=255)
#     isbn = models.DecimalField(decimal_places=0, max_digits=13)
#     categoria = models.ManyToManyField(Categoria,  related_name='livros')
#     editora = models.ForeignKey(Editora, on_delete=models.PROTECT ,related_name='livros')
#     autores = models.ManyToManyField(Autor,  related_name='livros')
#     localizacao = models.ForeignKey(Localização, on_delete=models.PROTECT, related_name='livros')
#     emprestimo = models.DateField(null=True, blank=True)
#     devolucao = models.DateField(null=True, blank=True)
#     capa = models.ForeignKey(
#         Image,
#         related_name="+",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         default=None,
#     )

#     def __str__(self):
#         return self.titulo
        