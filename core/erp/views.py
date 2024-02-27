from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def myfirstview(request):
    data = {
        'message': 'Hello',
        'name': 'Josue Ortiz'
    }
    return JsonResponse(data)

def indexview(request):
    return HttpResponse('Esta es la Página Principal')