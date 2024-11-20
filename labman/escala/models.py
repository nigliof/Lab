from django.db import models

# Create your models here.

class funcionario(models.Model):
    nome_completo = models.CharField(max_length=200)