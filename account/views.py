from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from main.views import index

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html', {
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                user.save()
                # Save session
                login(request, user)
                return redirect('project')
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
    return redirect(request, 'index')