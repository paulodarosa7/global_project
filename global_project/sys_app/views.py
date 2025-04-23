from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def viagens(request):
    return render(request, 'viagens.html')

def nova_viagem(request):
    return render(request, 'viagens_nova.html')



# def nova_viagem(request):
#     return render(request, 'templates/nova_viagem.html')

# def resumo_viagem(request):
#     return render(request, 'templates/resumo_viagem.html')

# def listar_viagens(request):
#     return render(request, 'templates/listar_viagens.html')

# def mensagem(request):
#    if request.method == 'POST':
#         destino = request.POST.get('destino')
#         return redirect(f'/resumo_viagem/?destino{destino}')
#         return render(request,'templates/resumo_viagem.html')