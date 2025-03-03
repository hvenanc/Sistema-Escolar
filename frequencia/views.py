from django.shortcuts import render, get_object_or_404, redirect
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from frequencia.models import Frequencia
from turmas.models import Turma
from aula.models import Aula


def lancar_frequencia_view(request, turma_id):
    try:
        turma = get_object_or_404(Turma, id=turma_id)
        alunos = turma.estudantes.all().order_by('nome')

        if request.method == 'POST':
            
            conteudo = request.POST.get('conteudo')
            data = request.POST.get('data')
            aula = Aula.objects.create(
                turma = turma,
                data = data,
                conteudo = conteudo
            )
            
            for aluno in alunos:
                presente = request.POST.get(f'presente_{aluno.id}') == 'on'
                Frequencia.objects.update_or_create(
                    aluno=aluno,
                    defaults={'presente': presente},
                    aula = aula
                )

            return redirect('frequencia:diario')

        return render(request, 'pages/frequencia.html', {
            'turma': turma,
            'alunos': alunos,
        })
    
    except IntegrityError:
        return render(request, 'pages/erro.html', {
            'mensagem' : 'Ops! A frequência da turma já foi registrada para hoje. Se precisar fazer alguma correção, entre em contato com o administrador.'
        })


def diarios_view(request):

    try:

        turmas = Turma.objects.all().order_by('nome')
        frequencia = []
        aula = None


        if request.method == 'POST':
            turma = request.POST.get('turma_id')
            data = request.POST.get('data')
            aula = Aula.objects.get(data = data, turma = turma)
            frequencia = Frequencia.objects.filter(aula = aula)
            print(frequencia)
        return render(request, 'pages/diario.html', {
            'turmas' : turmas,
            'frequencia' : frequencia,
            'aula': aula
        })
    
    except ObjectDoesNotExist:
        return render(request, 'pages/erro.html', {
            'mensagem' : 'Ops! Não existe nenhum diário para essa turma nesta data!'
        })
    

def relatorio_view(request):
    
    turmas = Turma.objects.all()
    turma = None
    aulas = []
    alunos = []
    frequencias = []
    frequencias_dict = {}
    if request.method == 'POST':
        turma_id = request.POST.get('turma_id')
        aulas = Aula.objects.filter(turma = turma_id).all().order_by('data')
        turma = Turma.objects.filter(id = turma_id).first()
        alunos = turma.estudantes.all().order_by('nome')
        frequencias_dict = {aluno.nome : [] for aluno in alunos}
        
        for aula in aulas:
            freq = Frequencia.objects.filter(aula = aula).all()
            frequencias.append(freq)

        
        for frequencia in frequencias:
            for x in frequencia:
                frequencias_dict[x.aluno.nome].append(x.presente)

    return render(request, 'pages/relatorio.html', {
        'turmas' : turmas,
        'aulas' : aulas,
        'alunos': alunos,
        'frequencias' : frequencias_dict,
        'turma' : turma
    })