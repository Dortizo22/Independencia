from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.erp.models import Category, Product
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
    data = {
        'name': 'Josue Ortiz',
        'categories': Category.objects.all(),
    }
    return render(request, 'index.html', data)

def indexbootstrap(request):
    return render(request, 'index_boostrap.html')

def index_adminlte(request):
    return render(request, 'body.html')


