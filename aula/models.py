from django.db import models
from turmas.models import Turma

class Aula(models.Model):

    conteudo = models.CharField(max_length=256)
    data = models.DateField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['turma', 'data'], name='unique_aula_por_turma_e_data')
        ]

    def __str__(self):
        return f"Aula de {self.data} - {self.turma}"

