from django.contrib import admin
from inscricao.models import Pessoa

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'idade']
    ordering = ('-idade',)
    search_fields = ('nome', 'telefone')


admin.site.register(Pessoa, PessoaAdmin)