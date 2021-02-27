from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ShipRegisterForm, CrewRegisterForm
from django.contrib import messages
from .models import Ship, Character, DashBoard_VM
import datetime
from ship import services as ship_services

def index(request, id):
    dash = ship_services.get_dashboard(id, 1)
    return render(request, 'ship/dashboard.html', {'characters': dash.ship.characters.all()})

def register(request):
    if request.method == 'POST':
        form = ShipRegisterForm(request.POST, request.user) 
        if form.is_valid():
            ship_services.register_ship(form, request.user)
            ## return data
            name = form.cleaned_data.get('ship_name')
            messages.success(request, f'User registered as {name} successfully. Enter your credentials to login.')
            return redirect('index')
    else:
        form = ShipRegisterForm()
    return render(request, 'ship/register.html', {'form': form})

def register_crew(request):
    if request.method == 'POST':
        form = CrewRegisterForm(request.POST, request.user) 
        if form.is_valid():
            registration = ship_services.register_crew(form, request.user)
            if registration:
                messages.success(request, f'User registered to crew as {request.user.username} successfully. Enter your credentials to login.')
            else:
                messages.error(request, f'Error joining crew, try again.')

            return redirect('index')
        else:
            form = CrewRegisterForm()
    else:
        form = CrewRegisterForm()
    return render(request, 'ship/register_crew.html', {'form': form})

