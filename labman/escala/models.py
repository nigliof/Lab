from django.db import models

# Create your models here.
sexo_choices = (("M", "MASCULINO"),("F", "FEMININO"))
tipo_evento_choices = (("TR", "TRABALHADO"),
                       ("FO", "FOLGA"),
                       ("FS", "FOLGA SAÚDE"),
                       ("DO", "DOBRA"),
                       ("BH", "BANCO DE HORAS"),
                       ("FE", "FERIAS")
                       )

status_do_evento_choices = (("PD", "PENDENTE"),("CO", "CONFIRMADO"))

class RegiaoGestao(models.Model):
    regiao_gestao = models.CharField(primary_key=True, max_length=200)
    
    def __str__(self):
        return self.regiao_gestao

class Cidades(models.Model):
    cidade = models.CharField(primary_key=True, max_length=200)
    regiao_gestao_cidades = models.ForeignKey(RegiaoGestao, on_delete=models.PROTECT)

    def __str__(self):
        return self.cidade

class Unidades(models.Model):
    nome_unidade = models.CharField(primary_key=True, max_length=200)
    cidade_unidades = models.ForeignKey(Cidades, on_delete=models.PROTECT)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_unidade

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
    sigla_turno_funcionario = models.ForeignKey(Turno, on_delete=models.PROTECT)
    unidade_funcionario = models.ForeignKey(Unidades, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_completo



# A classe abaixo é a princial classe para armazenar os Fatos referente ao planejamento e programação da escala

class ProgramacaoEscala(models.Model):
    nome_completo_prog = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    sigla_turno_prog = models.ForeignKey(Turno, on_delete=models.PROTECT)
    unidade_prog = models.ForeignKey(Unidades, on_delete=models.PROTECT)
    tipo_evento = models.CharField(max_length=15, choices=tipo_evento_choices)
    inicio_evento = models.DateTimeField()
    fim_evento = models.DateTimeField()
    status_do_evento = models.CharField(max_length=30, choices=status_do_evento_choices, default="PD")

    def __str__(self):
        return f"{self.nome_completo_prog} para o {self.unidade_prog}. Programação de {self.tipo_evento} inicio {self.inicio_evento} fim {self.fim_evento}. Status é {self.status_do_evento}."