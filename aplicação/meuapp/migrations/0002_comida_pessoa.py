# Generated by Django 3.1 on 2020-10-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('comida', models.ManyToManyField(to='meuapp.Comida')),
            ],
        ),
    ]
