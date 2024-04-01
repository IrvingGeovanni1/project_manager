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
    print(request.user)
    # Get User's Projects
    projects = Project.objects.filter(user=request.user)

    # Evaluate each project individually
    for project in projects:
        print('1Projecto original ' + str(project) + ' - Atributo complete ' + str(project.date_completed))
        tasks_count = project.task_set.count()
        completed_tasks_count = project.task_set.filter(date_completed__isnull=False).count()
    
        # If the project has not tasks or if all of its tasks are incomplete
        if tasks_count == 0 or tasks_count != completed_tasks_count:
            project.complete = False
            project.date_completed = None
            project.save()
            print('2Projecto modificado ' + str(project) + ' - Atributo complete ' + str(project.date_completed))
        else:
        # If the Project has all complete task    
            project.complete = True
            project.date_completed = timezone.now()
            project.save()
            print('3Projecto modificado ' + str(project) + ' - Atributo complete ' + str(project.date_completed))

    # If Project is uncomplete
    if project.complete:
        # Filter Projects for date completed
        projects_pending = projects.filter(user=request.user, date_completed__isnull=True)

        # Show list Projects
        return render(request, 'project/project.html',{
            'title': title,
            'projects': projects_pending
        })
    else:
    # If Project is complete
        projects = Project.objects.filter(user=request.user, date_completed__isnull=True)
        # Show list Projects
        return render(request, 'project/project.html', {
            'title': title,
            'projects': projects,
        })

# Show Projects completed
@login_required
def projects_completed(request):
    title = 'Completed Projects'

    # Get all User's Projects
    projects = Project.objects.filter(user=request.user)

    # Evaluate each project individually
    for project in projects:
        print('1Projecto original ' + str(project) + ' - Atributo complete ' + str(project.date_completed))
        tasks_count = project.task_set.count()
        completed_tasks_count = project.task_set.filter(date_completed__isnull=False).count()

        # If the project has all tasks complete
        if tasks_count == completed_tasks_count and tasks_count > 0:
            project.complete = True
            project.date_completed = timezone.now()
            project.save()
            print('2Proyecto modificado ' + str(project) + ' - Atributo complete ' + str(project.date_completed))

        else:
            project.complete= False
            project.date_completed = None
            project.save()
            print('3Proyecto modificado ' + str(project) + ' - Atributo complete ' + str(project.date_completed))

    # If Project is complete  
    if project.complete:
        # Filter Projects for date completed - Order by date_completed
        projects_completed = projects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
        
        return render(request, 'project/project.html', {
            'title': title,
            'projects':projects_completed,
        })
    else:
    # If Projects is uncomplete
        projects = Project.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')

        return render(request, 'project/project.html', {
            'title': title,
            'projects': projects,
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
                print(request.POST) # Impresión en consola
                project = get_object_or_404(Project, pk=project_id, user=request.user)
                form = ProjectForm(request.POST, request.FILES, instance=project)
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
    if request.method == 'POST':
        try:
            form = ProjectForm(request.POST, request.FILES) # Included function to manage images 
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'project/create_project.html', {
                'form': ProjectForm,
                'error': 'Please provide valida data',
            })
    else:
        form = ProjectForm()
        return render(request, 'project/create_project.html', {
                  'form': form,
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
        return redirect('home')
 
 