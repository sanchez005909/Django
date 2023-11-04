from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from main.models import Product, Category


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ('title',
              'description',
              'category',
              'image',
              'price',
              )
    template_name = 'main/product_form.html'
    success_url = '/'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('title',
              'description',
              'category',
              'image',
              'price',
              )
    template_name = 'main/product_form.html'
    success_url = '/'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_delete.html'
    success_url = '/'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


def contact(request):
    return render(request, 'main/contact.html')


