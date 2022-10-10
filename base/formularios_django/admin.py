

from django.contrib.admin import register, ModelAdmin

# Register your models here.
from base.formularios_django.models import Cliente


@register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'sexo', 'email')
    ordering = ('nome',)

