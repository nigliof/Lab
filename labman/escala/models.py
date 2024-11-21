from django.db import models

# Create your models here.
sexo_choices = (("M", "MASCULINO"),("F", "FEMININO"))

class Turno(models.Model):
    sigla_turno = models.CharField(primary_key=True, max_length=5)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    ativo = models.BooleanField

    def __str__(self):
        return self.sigla_turno

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=200)
    sexo = models.CharField(max_length=15, choices=sexo_choices, default="M")
    sigla_turno = models.ForeignKey(Turno, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_completo

