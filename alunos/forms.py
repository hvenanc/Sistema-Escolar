from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'email']

    nome = forms.CharField(
        required=True,
        label='Nome Completo',
        widget= forms.TextInput(attrs={
            'placeholder':'Nome Completo',
            'class': 'form-control',
        }),
    )

    matricula = forms.CharField(
        required=True,
        label='Matrícula',
        widget= forms.TextInput(attrs={
            'placeholder':'Matrícula',
            'class': 'form-control',
        }),
    )

    email = forms.CharField(
        required=True,
        label='E-mail Institucional',
        widget= forms.TextInput(attrs={
            'placeholder':'E-mail Institucional',
            'class': 'form-control',
        }),
    )