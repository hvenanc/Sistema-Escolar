from django.shortcuts import render, get_object_or_404, redirect
from .models import Frequencia
from turmas.models import Turma


def turma_detalhes(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    alunos = turma.estudantes.all().order_by('nome')

    if request.method == 'POST':
        for aluno in alunos:
            descricao = request.POST.get('descricao')
            data = request.POST.get('data')
            presente = request.POST.get(f'presente_{aluno.id}') == 'on'
            Frequencia.objects.update_or_create(
                aluno=aluno,
                data=data,
                defaults={'presente': presente},
                descricao = descricao
            )
        return redirect('turmas:detalhar', id=turma.id)

    return render(request, 'pages/frequencia.html', {
        'turma': turma,
        'alunos': alunos,
    })
