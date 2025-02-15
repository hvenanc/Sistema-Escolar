from django.db import models


class Aluno(models.Model):
    matricula = models.CharField(max_length=10, null=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome