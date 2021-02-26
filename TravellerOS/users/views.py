from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from ship.models import Ship

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User registered as {username} successfully. Enter your credentials to login.')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def index(request):
    if request.user.is_authenticated:
        ships = request.user.ship_set.all()
    else:
        ships = []
    context = {
        'ships': ships 
    }
    return render(request, 'users/index.html', {'ships': ships})
