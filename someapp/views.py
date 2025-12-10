from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator

def product_list(request):
    """Список всех товаров"""
    products = Product.objects.filter(in_stock=True)
    categories = Category.objects.all()
    
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'someapp/product_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': category_slug,
    })

def product_detail(request, pk):
    """Детальная информация о товаре"""
    product = get_object_or_404(Product, pk=pk, in_stock=True)
    return render(request, 'someapp/product_detail.html', {'product': product})

def category_products(request, slug):
    """Товары определенной категории"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, in_stock=True)
    return render(request, 'someapp/category_products.html', {
        'category': category,
        'products': products,
    })

def home(request):
    """Главная страница магазина"""
    featured_products = Product.objects.filter(in_stock=True)[:8]
    categories = Category.objects.all()
    return render(request, 'someapp/home.html', {
        'featured_products': featured_products,
        'categories': categories,
    })