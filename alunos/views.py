from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .forms import AlunoForm
from .models import Aluno


def listar_alunos(request):
   
   alunos = Aluno.objects.all()
   form = AlunoForm()
   return render(request, 'pages/alunos.html', {
      'alunos': alunos,
      'fields' : form,
      'form_action' : reverse('alunos:post')
   })


def form_cadastro_aluno(request):
   form = AlunoForm()
   return render(request, 'pages/formCadastro.html', {
      'title': 'Cadastro de Estudante',
      'fields' : form,
      'form_action' : reverse('alunos:post')
   })


def cadastrar_aluno(request):
   
   if not request.POST:
      raise Http404()
   
   aluno = AlunoForm(request.POST)
   if aluno.is_valid():
      nome = aluno.cleaned_data.get('nome', '')
      matricula = aluno.cleaned_data.get('matricula', '')
      email = aluno.cleaned_data.get('email', '')
      Aluno.objects.create(nome=nome, email=email, matricula=matricula)
      
   return redirect(reverse('alunos:alunos'))


def deletar_aluno(request, id):
   aluno = Aluno.objects.get(id = id)
   aluno.delete()
   return redirect(reverse('alunos:alunos'))


def form_editar_aluno(request, id):
   aluno = Aluno.objects.get(id = id)
   form = AlunoForm(instance = aluno)
   return render(request, 'pages/formEditar.html', {
      'aluno' : aluno,
      'title': 'Editar Estudante',
      'fields' : form,
      'form_action' : reverse('alunos:salvar', args=[aluno.id])
   })


def editar_aluno(request, id):
   
   aluno = AlunoForm(request.POST)
   if aluno.is_valid():
      nome = aluno.cleaned_data.get('nome', '')
      matricula = aluno.cleaned_data.get('matricula', '')
      email = aluno.cleaned_data.get('email', '')
      aluno = Aluno.objects.get(id = id)
      aluno.nome = nome
      aluno.matricula = matricula
      aluno.email = email
      aluno.save()

   return redirect(reverse('alunos:alunos'))

   