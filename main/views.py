from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from main.forms import ProductForm, VersionForm, CategoryForm
from main.models import Product, Category, Version
from main.services import get_cached_category


# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = 'main/category_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = get_cached_category()
        return context_data


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'main/category_form.html'
    success_url = reverse_lazy('main:category_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'main/category_form.html'
    success_url = reverse_lazy('main:category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'main/category_delete.html'
    success_url = reverse_lazy('main:category_list')


class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = '/'

    def form_valid(self, form):
        user = self.request.user
        if user.is_authenticated:
            self.object = form.save()
            self.object.user_prod = self.request.user
            self.object.save()
            return super().form_valid(form)

        else:
            return redirect(reverse_lazy('users:login'))


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'main.update_product'
    template_name = 'main/product_form.html'
    success_url = '/'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_staff:
            return self.object
        if self.object.user_prod != self.request.user:
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
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

    def test_func(self):
        return self.request.user.is_active


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'main/product_delete.html'
    success_url = '/'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


def contact(request):
    return render(request, 'main/contact.html')


def toggle_published(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_published:
        product_item.is_published = False
    else:
        product_item.is_published = True

    product_item.save()

    return redirect(reverse('main:main'))
