from django.urls import path
from turmas.views import *

app_name = 'turmas'

urlpatterns = [
    path('', listar_turmas, name='turmas'),
    path('novo/', form_cadastrar_turma, name='cadastrar'),
    path('cadastrar/', cadastrar_turma, name = 'salvar'),
    path('deletar/<int:id>', deletar_turma, name='deletar'),
    path('editar/<int:id>', form_editar_turma, name='editar'),
    path('editarT/<int:id>', editar_turma, name='editar_turma'),
    path('detalhar/<int:id>', detalhar_turma, name='detalhar'),
    path('detalhar/<int:turma_id>/adicionarEstudante', adicionar_estudante, name='estudante'),
]