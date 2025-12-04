from django.db import models

class Category(models.Model):
    """Категория товаров (например: Футболки, Джинсы, Платья)"""
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """Товар (одежда)"""
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, verbose_name="Размер")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    material = models.CharField(max_length=100, verbose_name="Материал")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение", blank=True)
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    def __str__(self):
        return f"{self.name} - {self.size}"