from django.urls import path
from frequencia.views import *

app_name = 'frequencia'

urlpatterns = [
    path('<int:turma_id>/', turma_detalhes, name='frequencia'),
    path('diarios/', diarios_view, name='diario')
]