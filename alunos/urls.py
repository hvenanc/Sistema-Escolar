from django.urls import path
from alunos.views import *


app_name = 'alunos'

urlpatterns = [
    path('', listar_alunos, name = 'alunos'),
    path('novo/', form_cadastro_aluno, name='cadastrar'),
    path('cadastrar/', cadastrar_aluno, name='post'),
    path('deletar/<int:id>', deletar_aluno, name='deletar'),
    path('editar/<int:id>', form_editar_aluno, name='editar'),
    path('salvar/<int:id>', editar_aluno, name='salvar'),
]