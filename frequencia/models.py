from django.db import models
from alunos.models import Aluno
from aula.models import Aula


class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="frequencias")
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name="aulas")
    presente = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.aluno.nome} - {'Presente' if self.presente else 'Falta'}"