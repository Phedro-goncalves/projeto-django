from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def Home(request):
    return render(request,'recipes/home.html', context={
        'name': 'Pedro Henrique'
    })

def contato(request):
    return render(request,'me-apague/temp.html')

def sobre(request):
    return HttpResponse('Sobre')