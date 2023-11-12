from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from main.forms import ProductForm, VersionForm
from main.models import Product, Category, Version


# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = 'main/index.html'


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = '/'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1 )
        context_data['formset'] = VersionFormset()
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/product_delete.html'
    success_url = '/'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


def contact(request):
    return render(request, 'main/contact.html')


