from django.shortcuts import render,redirect,get_object_or_404
from .models import viagem

VIAGENS = []
PROXIMO_ID = 1

# Create your views here.
def home(request):
    return render(request, 'home.html')


def viagens(request):
    return render(request, 'viagens.html', {'viagens': VIAGENS})


def nova_viagem(request):
    global PROXIMO_ID
    if request.method == 'POST':
        destino   = request.POST['destino']
        data_ida  = request.POST['data_ida']
        data_volta= request.POST['data_volta']
        #cria dict com ID unico
        viagem = {
            'id': PROXIMO_ID,
            'destino': destino,
            'data_ida': data_ida,
            'data_volta': data_volta,
        }
        VIAGENS.append(viagem)
        PROXIMO_ID += 1
        return redirect('detalhar_viagem', id=viagem['id'])
    return render(request, 'viagens_nova.html')


def detalhar_viagem(request, id):
    viagem = next((v for v in VIAGENS if v['id']==id), None)
    if not viagem:
        return render(request, '404.html', status=404)
    return render(request, 'detalhes_viagem.html', {'viagem': viagem})


def excluir_viagem(request, id):
    if request.method == 'POST':
        global VIAGENS
        VIAGENS = [v for v in VIAGENS if v['id'] != id]
        return redirect('listar_viagens')
    viagem = next((v for v in VIAGENS if v['id']==id), None)
    if not viagem:
        return render(request, '404.html', status=404)
    return render(request, 'excluir_viagem.html', {'viagem': viagem})