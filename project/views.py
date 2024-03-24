from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm
from .models import Project
from task.models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

"""@login_required -> This code protected the access of especific functions"""

# Show Projects pending
@login_required
def project(request):
    title = 'Pending Projects'
    projects = Project.objects.filter(user=request.user, date_completed__isnull=True)
    # Show list Projects
    return render(request, 'project/project.html',{
        'title': title,
        'projects': projects
    })

# Show Projects completed
@login_required
def projects_completed(request):
    title = 'Completed Projects'
    # Order by date completed
    projects = Project.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'project/project.html', {
        'title': title,
        'projects':projects
    })

# Show detail for proyect_id
@login_required
def project_detail(request, project_id):
        if request.method == 'GET':
             # Searching model project
            project = get_object_or_404(Project, pk = project_id, user=request.user)
            tasks = Task.objects.filter(project_id = project_id)
            # Create Project Form from Project Detail
            form = ProjectForm(instance=project)
            return render(request, 'project/project_detail.html', {
                'project': project,
                'tasks': tasks,
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
@login_required
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
@login_required
def complete_project(request, project_id):
    project = get_object_or_404 (Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        # Update field Date Complete
        project.date_completed = timezone.now()
        project.save()
        return redirect('projects')
    
# Return to uncompleted Project
@login_required
def uncomplete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        # Uncomplete Project
        project.date_completed = None
        project.save()
        return redirect('projects_completed')
    
# Delete Project
@login_required
def delete_project(request, project_id):
    project = get_object_or_404 (Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('index')