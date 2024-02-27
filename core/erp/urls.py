from django.urls import path
from core.erp.views import myfirstview, mysecondview, pruebaview

urlpatterns = [
    path('', pruebaview),
    path('uno/', myfirstview),
    path('dos/', mysecondview),
]