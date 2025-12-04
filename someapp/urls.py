from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('category/<slug:slug>/', category_products, name='category_products'),
]