from django.shortcuts import render

from products.models import Products


# Create your views here.
def index(request):
    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/index.html', context=context)
