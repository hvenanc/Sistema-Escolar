from django import forms
from .models import Turma


class TurmaForm(forms.ModelForm):

    class Meta:
        model = Turma
        fields = ['nome', 'descricao', 'horario']

    nome = forms.CharField(
        required = True,
        label = 'Título da Turma',
        widget = forms.TextInput(attrs={
            'placeholder': 'Título da Turma',
            'class': 'form-control',
        }),
    )

    descricao = forms.CharField(
        required = True,
        label = 'Descrição da Turma',
        widget = forms.TextInput(attrs={
            'placeholder': 'Descrição da Turma',
            'class': 'form-control',
        }),
    )

    horario = forms.CharField(
        required = True,
        label = 'Horário de Aula',
        widget = forms.TextInput(attrs={
            'placeholder': 'Horário de Aula',
            'class': 'form-control',
        }),
    )

