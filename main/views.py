from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Product, Category


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


def contact(request):
    return render(request, 'main/contact.html')