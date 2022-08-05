from re import search
from django.urls import path
from products.views import list_products, create_product, primer_form, search_products, delete_product, update_product


urlpatterns = [
    path('create_product/', create_product, name="create_product"),
    path('list_products/', list_products, name="list_products"),
    path('primer_formulario/', primer_form, name="primer_formulario"),
    path('search-products/', search_products, name="search_products"),
    path('delete-product/<int:pk>/', delete_product, name="delete_product"),
    path('update-product/<int:pk>/', update_product, name="update_product"),
]
