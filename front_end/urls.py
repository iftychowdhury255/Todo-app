from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Complete/<int:pk>/', views.statusComplete, name='statusComplete'),
    
]
