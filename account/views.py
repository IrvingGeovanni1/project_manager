from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth.models import User
from account.models import User #UserCustome
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .forms import UserForm

# Create Account's views

def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html', {
        'form': UserCreationForm,
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                user.save()
                # Save session
                login(request, user)
                return redirect('projects')
            except IntegrityError:
                return render(request, 'account/signup.html', {
                'form': UserCreationForm,
                'error': 'Username already exists'
        })
        else:
            return render(request, 'account/signup.html', {
                'form': UserCreationForm,
                'error': 'Password do not match'
            })

def signin(request):
    # Authentication Form
    if request.method == 'GET':
        return render(request, 'account/signin.html', {
        'form': AuthenticationForm
        })
    else:
        # Authentication
        user = authenticate( request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'account/signin.html', {
            'form': AuthenticationForm,
            'error': 'Username or password es incorrect'
            })  
        else:
            # Save session
            login(request, user)
            return redirect('projects')  

def signout(request):
    logout(request)
    return redirect('home')

def profile(request):
    title ='s Profile'
    if request.method == 'GET':
        print('Usuario del request: ' + str(request.user))
        user_profile = get_object_or_404(User, username = request.user)
        print(user_profile)
        return render(request, 'account/profile.html', {
            'title': title,
            'user': user_profile,
        })
    
def update_profile(request):
    title_page = 'Editing profile - PM'
    user = get_object_or_404(User, pk=request.user.id)  # Obtén el usuario actual
    if request.method == 'GET':
        form = UserForm(instance=user)  # Crea una instancia del formulario
        return render(request, 'account/update_profile.html', {
            'form': form,
            'user': user
            })
    else:
        try:
            form = UserForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        except ValueError:
            return render(request, 'account/profile.html', {
                'user': user,
                'form': form,
                'error': 'Error al actualizar el usuario',
            })