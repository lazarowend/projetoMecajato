# Generated by Django 4.2.2 on 2023-06-26 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaManutenção',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('TDO', 'Troca de óleo'), ('TDP', 'Troca de pneus'), ('B', 'Balanceamento'), ('SDF', 'Serviço de freios'), ('TDC', 'Troca de correias'), ('RSE', 'Reparo do sistema de escape'), ('S', 'Suspensão'), ('TB', 'Troca de bateria')], max_length=3)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField(max_length=200)),
                ('data_inicio', models.DateField(null=True)),
                ('data_fim', models.DateField(null=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('protocolo', models.CharField(blank=True, max_length=32, null=True)),
                ('categoria_manutencao', models.ManyToManyField(to='servicos.categoriamanutenção')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.cliente')),
            ],
        ),
    ]
