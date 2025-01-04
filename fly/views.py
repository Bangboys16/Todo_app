from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm 


def home(request):
    task = Task.objects.all()
    return render(request, 'fly/index.html', {'task': task})


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'fly/todo_detail.html', {'task': task})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
  
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'fly/todo_delete.html', {'task': task})


def task_update(request, id):
    task = get_object_or_404(Task, id=id)  
   

    if request.method == 'POST':
         form = TaskForm(request.POST, instance=task)
         if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TaskForm(instance=task)

    return render(request, 'fly/update_todo.html', {'form': form})


def create_task(request):
    
    if request.method == 'POST':
         form = TaskForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TaskForm()

    return render(request, 'fly/create_todo.html', {'form': form})

