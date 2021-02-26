from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ship_index'),
    path('register/', views.register, name='ship_register'),
    path('join/', views.register_crew, name='crew_register'),
]