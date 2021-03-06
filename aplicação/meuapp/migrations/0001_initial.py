# Generated by Django 3.1 on 2020-10-16 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pintor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nascimento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quadro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacao', models.DateTimeField()),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('pintor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuapp.pintor')),
            ],
        ),
    ]
