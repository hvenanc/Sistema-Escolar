from django.urls import path
from frequencia.views import *

app_name = 'frequencia'

urlpatterns = [
    path('<int:turma_id>/', lancar_frequencia_view, name='frequencia'),
    path('diarios/', diarios_view, name='diario'),
    path('relatorio/', relatorio_view, name='relatorio')
]