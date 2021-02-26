from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ShipRegisterForm, CrewRegisterForm
from django.contrib import messages
from .models import Ship

def index(request):
    return HttpResponse("Hello, world. You're at the ship index.")

def register(request):
    if request.method == 'POST':
        form = ShipRegisterForm(request.POST, request.user) 
        if form.is_valid():
            ship = form.save(commit=False)
            ship.save()
            ship.users.add(request.user)
            form.save_m2m()
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
            ship = Ship.objects.filter(ship_code=form.cleaned_data.get('ship_code'))
            if len(ship) == 1:
                ship.first().users.add(request.user)
                ship.first().save()
                messages.success(request, f'User registered to crew as {request.user.username} successfully. Enter your credentials to login.')
            else:
                messages.error(request, 'There was an issue join that ship code. Try again')
            return redirect('index')
    else:
        form = CrewRegisterForm()
    return render(request, 'ship/register_crew.html', {'form': form})

