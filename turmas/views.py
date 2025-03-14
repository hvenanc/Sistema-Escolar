from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .models import Turma, Aluno
from .forms import TurmaForm


def listar_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'pages/turmas.html', {
        'turmas': turmas
    })


def form_cadastrar_turma(request):
    form = TurmaForm()
    return render(request, 'pages/formCadastro.html', {
        'fields': form,
        'title': 'Cadastro de Turma',
        'form_action': reverse('turmas:salvar')
    })


def cadastrar_turma(request):
    
    if not request.POST:
        raise Http404()

    turma = TurmaForm(request.POST)

    if turma.is_valid():
        nome = turma.cleaned_data.get('nome', '')
        descricao = turma.cleaned_data.get('descricao', '')
        horario = turma.cleaned_data.get('horario', '')
        Turma.objects.create(
            nome = nome,
            descricao = descricao,
            horario = horario
        )
    return redirect(reverse('turmas:turmas'))


def deletar_turma(request, id):

    turma = Turma.objects.get(id = id)
    turma.delete()
    return redirect(reverse('turmas:turmas'))


def form_editar_turma(request, id):

    turma = Turma.objects.get(id = id)
    form = TurmaForm(instance=turma)
    return render(request, 'pages/formEditar.html', {
        'turma': turma,
        'fields' : form,
        'title' : 'Editar Dados da Turma',
        'form_action' : reverse('turmas:editar_turma', args=[turma.id])
    })


def editar_turma(request, id):

    turma = TurmaForm(request.POST)

    if turma.is_valid():
        nome = turma.cleaned_data.get('nome', '')
        descricao = turma.cleaned_data.get('descricao', '')
        horario = turma.cleaned_data.get('horario', '')
        turma = Turma.objects.get(id = id)
        turma.nome = nome
        turma.descricao = descricao
        turma.horario = horario
        turma.save()

    return redirect(reverse('turmas:turmas'))


def detalhar_turma(request, id):

    turma = Turma.objects.get(id = id)
    alunos = turma.estudantes.all().order_by('nome')
    estudantes = Aluno.objects.exclude(turma=turma) 

    return render(request, 'pages/detalharTurma.html', {
        'turma': turma,
        'estudantes': estudantes,
        'alunos' : alunos,
        'form_action': reverse('turmas:estudante', args=[turma.id])
    })


def adicionar_estudante(request, turma_id):

    turma = Turma.objects.get(id = turma_id)

    if request.method == "POST":
        estudante_id = request.POST.get("estudante_id")
        estudante = Aluno.objects.get(id = estudante_id)

        turma.estudantes.add(estudante)

        return redirect(reverse('turmas:detalhar', args=[turma.id]))
    
    return render(request, "detalharTurma.html", {
        "turma": turma
    })