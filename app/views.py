from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import generic
from .forms import CustomUserCreationForm


#  Testing Class Based Views
class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = '/dashboard'
    template_name = 'authentication/register.html'


# GET Request for login form
def get_login_form(request):
    return render(request, 'authentication/login.html')


# POST Request to authenticate users
def authenticate_user(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        messages.error(request, 'Email or password is not recognized')
        return redirect('/login')


# GET Dashboard
def get_dashboard(request):
    pass


# Dashboard
def dashboard(request):
    return render(request, 'dashboard.html', {})


# POST Request Add post
def add_post(request):
    return redirect('/')
