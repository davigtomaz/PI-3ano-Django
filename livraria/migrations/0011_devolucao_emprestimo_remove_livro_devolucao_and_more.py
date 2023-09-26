# Generated by Django 4.2.5 on 2023-09-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0010_itenscarrinho"),
    ]

    operations = [
        migrations.CreateModel(
            name="Devolucao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("dia", models.DateField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Devoluções",
            },
        ),
        migrations.CreateModel(
            name="Emprestimo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("dia", models.DateField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Empréstimos",
            },
        ),
        migrations.RemoveField(
            model_name="livro",
            name="devolucao",
        ),
        migrations.RemoveField(
            model_name="livro",
            name="emprestimo",
        ),
        migrations.RemoveField(
            model_name="livro",
            name="isbn",
        ),
    ]
