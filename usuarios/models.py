from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    peso = models.FloatField()
    altura = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome


class clientes_exercicios(models.Model):
    braco = models.CharField(max_length=100)
    perna = models.CharField(max_length=100)
    peito = models.CharField(max_length=100)
    costa = models.CharField(max_length=100)
    gluteo = models.CharField(max_length=100)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.cliente


