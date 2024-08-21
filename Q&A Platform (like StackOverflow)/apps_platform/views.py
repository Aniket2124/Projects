from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Answer, Question
from .forms import QuestionForm, AnswerForm, RegisterUserForm
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registred Successfully.')
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'apps_platform/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! You are now logged in.')
            return redirect('home')

        #     username = form.cleaned_data.get('username')
        #     password = form.cleaned_data.get('password')
        #     user = authenticate(request, username=username, password=password)
            
        #     if user is not None:
        #         login(request, user)
        #         return redirect('/')
        #     else:
        #         messages.error(request, 'Invalid username or password.')
        else:
            form = AuthenticationForm()
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'apps_platform/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'apps_platform/home.html')



   
