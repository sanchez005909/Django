from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from materials.models import Material


# Create your views here.

class MaterialListView(ListView):
    model = Material
    template_name = 'materials/material_list.html'


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title',
              'description',
              'image',
              'is_published',
              )
    template_name = 'materials/material_form.html'
    success_url = '/materials/'


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title',
              'description',
              'image',
              'is_published',
              )
    template_name = 'materials/material_form.html'
    success_url = '/materials/'


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materials/material_detail.html'


class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'materials/material_delete.html'
    success_url = '/materials/'

