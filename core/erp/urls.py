from django.urls import path
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category-list'),
    path('category/list2/', category_list, name='category-list2')
]