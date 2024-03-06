from djangoProject.wsgi import *
from core.erp.models import *

data = ['leche y derivados', 'Carnes, pescado y huevos', 'Patatas, legumbres y frutos secos',
        'verduras y hortalizas', 'frutas', 'Cereales y derivados', 'azucar y dulces',
        'Grasas, aceite y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))