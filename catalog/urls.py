from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, product_info, products_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('contacts/', contacts),
    path('product/<int:pk>/', product_info, name='product_info')
]
