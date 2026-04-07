from django.shortcuts import render,redirect
from task.models import Tarefa

def index(request):
    return render(request, 'task/index.html')

def task_list(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'task/tasks.html', {'tarefas':tarefas})

def create_task(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        data = request.POST.get('data')
        descricao = request.POST.get('descricao')
        status = False

        Tarefa.objects.create(titulo=titulo, descricao=descricao, data=data, status=status)
        return redirect('tasks')
    
    return render(request, 'task/create_task.html')

def delete_task(request, id):
    Tarefa.objects.get(id=id).delete()
    return redirect('tasks')
     

def edit_task(request, id):
    tarefa = Tarefa.objects.get(id=id)

    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.data = request.POST.get('data')
        tarefa.status = 'status' in request.POST
        tarefa.save()
        return redirect('tasks')
    
    return redirect('tasks')