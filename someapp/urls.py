from django.urls import path
from .views import home, product_list, product_detail

urlpatterns = [
    path('', home, name='home'),  # главная страница по адресу /
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]