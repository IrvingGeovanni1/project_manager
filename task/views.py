from django.shortcuts import render, redirect
from .forms import TaskForm

# Create your views here.

def task(request):
    return render(request, 'task/task.html')

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