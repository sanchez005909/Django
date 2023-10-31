from django.shortcuts import render

from main.models import Product, Category


# Create your views here.

def index(request):
    product_list = Product.objects.all()
    context = {
        'obj_list': product_list
    }
    return render(request, 'main/index.html', context)

def contact(requst):
    return render(requst, 'main/contact.html')