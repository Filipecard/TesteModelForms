from django.db import models

# Create your models here.


class Pintor(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Quadro(models.Model):
    publicacao = models.DateTimeField()
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    pintor = models.ForeignKey(Pintor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Comida(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    comida = models.ManyToManyField(Comida)

    def __str__(self):
        return self.nome