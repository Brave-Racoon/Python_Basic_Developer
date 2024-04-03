from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from products.models import Products


# Create your views here.
def index(request):
    return render(request, 'products/index.html')


def productslist(request):
    return render(request, 'products/products_list.html')


class ProductsListView(ListView):
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductsDetailView(DetailView):
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
