from django.db import models
from datetime import datetime

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Empleado(models.Model):
    categoria = models.ManyToManyField(Categoria)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
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

