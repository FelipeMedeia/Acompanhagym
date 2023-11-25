from django.contrib import admin
from .models import Clientes, Exercicios


# Register your models here.
@admin.register(Clientes)
class Clientesadmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'data_nascimento',
                    'email', 'peso', 'altura', 'user']


@admin.register(Exercicios)
class Exerciciosadmin(admin.ModelAdmin):
    list_display = ['braco', 'perna', 'peito',
                    'costa', 'gluteo', 'data', 'cliente', 'cliente_id']