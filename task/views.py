from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from project.models import Project

from django.contrib.auth.decorators import login_required
from django.utils import timezone

"""@login_required -> This code protected the access of especific functions"""

# Show Tasks pending.
@login_required
def task(request):
    title = 'Pending Tasks'
    pro = Project.objects.filter(user= request.user)
    # Filter Tasks by User
    tasks = Task.objects.filter(date_completed__isnull=True, project__in = pro)
    # Show list Tasks
    #no_pending_tasks = not tasks.exists()
    """print(no_pending_tasks)
    if not no_pending_tasks:
        for task in tasks:
            print('Título:', task.title, '| Fecha de completado:', task.date_completed)"""
    return render(request, 'task/task.html', {
        'title': title,
        'tasks': tasks,
    })

# Show Tasks Completed
@login_required
def tasks_completed(request):
    title = 'Completed Tasks'
    pro = Project.objects.filter(user=request.user)
    # Order by date completed
    tasks = Task.objects.filter(date_completed__isnull=False, project__in = pro).order_by('-date_completed')
    no_completed_tasks = not tasks.exists()
    """print(no_completed_tasks)
    if not no_completed_tasks:
        for task in tasks:
            print('Titulo:', task.title, '| Fecha de completado:', task.date_completed)"""
    return render(request, 'task/task.html', {
        'title': title,
        'tasks': tasks,
    })

# Show detail for task_id
@login_required
def task_detail(request,task_id):
    if request.method == 'GET':
        # Searching model task
        task = get_object_or_404(Task, pk = task_id)
        # Create Task Form from Task Detail
        form = TaskForm(instance=task, user = request.user)
        return render(request, 'task/task_detail.html', {
            'task': task,
            'form': form,
        })
    else:
        try:
            # Update Task
            task = get_object_or_404(Task, pk=task_id)
            form = TaskForm(request.POST, instance=task, user = request.user)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task/task_detail.html',{
                'task': task,
                'form': form,
                'error': "Error updating Task"
            })

# Create Task        
@login_required
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
            return redirect('projects')
        except ValueError:
            return render(request, 'task/create_task.html',{
                'form': TaskForm,
                'error': 'Please provide valida data'
            })
        
# Complete Task
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        # Update field Date Complete
        task.date_completed = timezone.now()
        task.save()
        return redirect('tasks')

# Return to uncompleted Task
@login_required
def uncomplete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        # Uncomplete Task
        task.date_completed = None
        task.save()
        return redirect('tasks_completed')

# Delete Task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    project = task.project
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', project.project_id)
