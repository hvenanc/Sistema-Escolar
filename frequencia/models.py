from django.db import models
from alunos.models import Aluno


class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="frequencias")
    data = models.DateField()
    descricao = models.CharField(max_length=256, null=True)
    presente = models.BooleanField(default=True)  # False = falta


    def __str__(self):
        return f"{self.aluno.nome} - {self.data} - {'Presente' if self.presente else 'Falta'}"