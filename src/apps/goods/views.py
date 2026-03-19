from django.shortcuts import render

from src.apps.goods.models import Products

def catalog(request):
    context = {
        'title': 'Home - Каталог',
        'goods': Products.objects.all()
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
