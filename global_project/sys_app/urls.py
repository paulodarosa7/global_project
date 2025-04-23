from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viagens/nova/', views.nova_viagem, name='nova_viagem'),
    path('viagens/', views.viagens, name='viagens'),

]