from django.db import models
from datetime import datetime

# Create your models here.
class Empleado(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='nombres')
    cedula = models.CharField(max_length=10, verbose_name='cedula', unique=True)
    fecha_registro = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    edad = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.BooleanField(default=True)
    #sexo = models.CharField(max_length=50, verbose_name='sexo')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    curriculum = models.FileField(upload_to='curriculum/%Y/%m/%d', null=True, blank=True)

def __str__(self):
    return self.nombres

class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    db_table = 'empleado'
    ordering = ['id']

