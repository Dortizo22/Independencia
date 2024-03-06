from djangoProject.wsgi import *
from django.test import TestCase
from core.erp.models import Tipo

#LISTAR

#Select * from table
#consulta = Tipo.objects.all()
#print(consulta)

#insert
#t = Tipo(nombre='Prueba2')
#t.nombre = 'Prueba'
#t.save()

#edicion
#t2 = Tipo.objects.get(id=2)
#t2.nombre = "Programador"
#t2.save()

#Eliminación

#t = Tipo.objects.get(id=4)
#t.delete()

#Filtrar una lista
#obj = Tipo.objects.filter(nombre__icontains='pr')
#obj = Tipo.objects.filter(nombre__endswith='r')
#obj = Tipo.objects.filter(nombre__endswith='r').query
obj = Tipo.objects.filter(nombre__endswith='r').exclude(id=2)

print(obj)