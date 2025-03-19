from django.shortcuts import render
from django.db.models import Prefetch
from category.models import Category, Region
from product.models import Product, ProductImage

def main(request):
    # Barcha kategoriyalarni olish
    

    # Asosiy kategoriyalarni olish
    categories = Category.objects.filter(is_main=True)

    # Asosiy rasmlar bilan birga mahsulotlarni olish
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images')
    )
    region = Region.objects.all()

    print(products)

    # Kontekstni shakllantirish
    ctx = {
        "categories": categories,
        "products": products,
        "regions": region,
        
    }

    return render(request, 'index-2.html', ctx)
