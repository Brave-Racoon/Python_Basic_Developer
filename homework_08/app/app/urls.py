"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

import products.views as views
from products.views import ProductsListView, ProductsDetailView

urlpatterns = [
    # associate path with views
    path('', views.index, name='index'),
    path("favicon.ico", RedirectView.as_view(url='static/favicon.ico')),
    path('products/', ProductsListView.as_view(), name='product-list'),
    path('products/<pk>/', ProductsDetailView.as_view(), name='product-detail'),
    path('admin/', admin.site.urls),
]


