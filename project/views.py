from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm
from .models import Project
from django.views.generic.detail import DetailView

# Create your views here.

def project(request):
    # Show list Projects
    projects = Project.objects.filter(user=request.user)
    return render(request, 'project/project.html',{
        'projects': projects
    })

# Show detail for proyect_id

def project_detail(request, project_id):
        if request.method == 'GET':
             # Searching model project
            project = get_object_or_404(Project, pk = project_id, user=request.user)
            # Create Project Form from Project Detail
            form = ProjectForm(instance=project)
            return render(request, 'project/project_detail.html', {
                'project': project,
                'form': form
            })
        else:
             try:
                # Update Project
                print(request.POST) # Impresión en consola
                project = get_object_or_404(Project, pk=project_id, user=request.user)
                form = ProjectForm(request.POST, instance=project)
                form.save()
                return redirect('projects')
             except ValueError:
                 return render(request, 'project/project_detail.html',{
                     'project': project,
                     'form': form,
                     'error': "Error updating projects"
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
        
