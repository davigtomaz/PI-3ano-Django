# Generated by Django 4.2.5 on 2023-11-08 14:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0003_emprestimo_nome_livro"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="emprestimo",
            name="nome_livro",
        ),
    ]
