from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def myfirstview(request):
    data = {
        'message': 'Hello',
        'name': 'Josue Ortiz'
    }
    return JsonResponse({'message': data['message']})

def mysecondview(request):
    data = {
        'message': 'Hello',
        'name': 'Josue Ortiz'
    }
    return JsonResponse({'name': data['name']})

def pruebaview(request):
    return HttpResponse('Pagina Principal de Prueba')

def indexview(request):
    return HttpResponse('Esta es la Página Principal')