from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project

# Create your views here.

def project(request):
    # Show list Project
    projects = Project.objects.filter(user=request.user)
    return render(request, 'project/project.html',{
        'projects': projects
    })

def create_project(request):
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {
                  'form': ProjectForm,
                  })
    else:
        try:
            form = ProjectForm(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'project/create_project.html', {
                'form': ProjectForm,
                'error': 'Please provide valida data',
            })