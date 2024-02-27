from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.

def task(request):
    # Shoe list Tasks
    tasks = Task.objects.all()
    return render(request, 'task/task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'task/create_task.html', {
            'form': TaskForm,
        })
    else:
        try:

            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task/create_task.html',{
                'form': TaskForm,
                'error': 'Please provide valida data'
            })