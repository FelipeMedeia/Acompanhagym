from django.contrib import admin
from .models import Clientes


# Register your models here.
@admin.register(Clientes)
class Clientesadmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'data_nascimento',
                    'email', 'peso', 'altura']
