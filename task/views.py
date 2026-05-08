from django.shortcuts import render,redirect, get_object_or_404
from task.models import Tarefa
from task.forms import TarefaForm
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tarefas = Tarefa.objects.filter(usuario = request.user)
    return render(request, 'task/tasks.html', {'tarefas':tarefas})

@login_required
def create_task(request):
    form = TarefaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            tarefa = form.save(commit= False)
            tarefa.usuario = request.user
            tarefa.save()
        return redirect('index')
        
    return render(request, 'task/tasks.html', {'tarefa':form})

@login_required
def delete_task(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario = request.user)
    tarefa.delete()
    return redirect('index')
     
@login_required
def edit_task(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario = request.user)
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.data = request.POST.get('data')
        tarefa.status = 'status' in request.POST
        tarefa.save()
        return redirect('index')
    
    return redirect('index')