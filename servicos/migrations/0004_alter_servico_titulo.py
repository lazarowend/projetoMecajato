# Generated by Django 4.2.2 on 2023-06-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_remove_servico_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
