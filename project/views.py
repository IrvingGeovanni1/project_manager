from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm
from .models import Project
from django.utils import timezone

# Show Projects pending
def project(request):
    # Show list Projects
    projects = Project.objects.filter(user=request.user, date_complete__isnull=True)
    return render(request, 'project/project.html',{
        'projects': projects
    })

# Show Projects completed
def projects_completed(request):
    # Order by date completed
    projects = Project.objects.filter(user=request.user, date_complete__isnull=False).order_by('-date_complete')
    return render(request, 'project/project.html', {
        'projects':projects
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
                #print(request.POST) # Impresión en consola
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

# Create new Project
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

# Complete Project 
def complete_project(request, project_id):
    project = get_object_or_404 (Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        # Update field Date Complete
        project.date_complete = timezone.now()
        print("Posterio DC: " + str(project.date_complete))
        project.save()
        return redirect('projects')
    
# Delete Project
def delete_project(request, project_id):
    project = get_object_or_404 (Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')