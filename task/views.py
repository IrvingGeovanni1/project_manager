from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

from django.contrib.auth.decorators import login_required

"""@login_required -> This code protected the access of especific functions"""

# Create your views here.

def task(request):
    # Show list Tasks
    tasks = Task.objects.all()
    return render(request, 'task/task.html', {
        'tasks': tasks
    })

# Show detail for task_id

def task_detail(request,task_id):
    # Searching model task
    task = get_object_or_404(Task, pk = task_id)
    return render(request, 'task/task_detail.html', {
        'task': task
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