from django.db import models
from alunos.models import Aluno

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    estudantes = models.ManyToManyField(Aluno)


    def __str__(self):
        return f'{self.nome} - {self.estudantes}'
