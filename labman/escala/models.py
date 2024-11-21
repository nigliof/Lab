from django.db import models

# Create your models here.
sexo_choices = (("M", "MASCULINO"),("F", "FEMININO"))

class funcionario(models.Model):
    nome_completo = models.CharField(max_length=200)
    sexo = models.CharField(max_length=15, choices=sexo_choices, default="M")