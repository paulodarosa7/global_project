from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('viagens/nova/',  views.nova_viagem, name='nova_viagem'),
    path('viagens/',  views.viagens, name='viagens'),

    path('viagens/<int:id>/', views.detalhar_viagem, name='detalhar_viagem'),
    path('viagens/<int:id>/excluir/', views.excluir_viagem, name='excluir_viagem'),

]