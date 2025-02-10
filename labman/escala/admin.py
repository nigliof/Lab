from django.contrib import admin
from .models import Funcionario, Turno, RegiaoGestao, Cidades, Unidades, ProgramacaoEscala

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Turno)
admin.site.register(RegiaoGestao)
admin.site.register(Cidades)
admin.site.register(Unidades)
admin.site.register(ProgramacaoEscala)
