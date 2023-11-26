from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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
        return f'{self.nome}'


class Exercicios(models.Model):
    EXERCICIO_CHOICES = (
        ("3 séries, 8 repetições", "3 séries, 8 repetições"),
        ("3 séries, 12 repetições", "3 séries, 12 repetições"),
        ("3 séries, 15 repetições", "3 séries, 15 repetições"),
        ("4 séries, 8 repetições", "4 séries, 8 repetições"),
        ("4 séries, 12 repetições", "4 séries, 12 repetições"),
        ("4 séries, 15 repetições", "4 séries, 15 repetições")
    )
    braco = models.CharField(default='-------', max_length=100, choices=EXERCICIO_CHOICES, null=True, blank=True)
    perna = models.CharField(default='-------', max_length=100, choices=EXERCICIO_CHOICES, null=True, blank=True)
    peito = models.CharField(default='-------', max_length=100, choices=EXERCICIO_CHOICES, null=True, blank=True)
    costa = models.CharField(default='-------', max_length=100, choices=EXERCICIO_CHOICES, null=True, blank=True)
    gluteo = models.CharField(default='-------', max_length=100, choices=EXERCICIO_CHOICES, null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.cliente}'
