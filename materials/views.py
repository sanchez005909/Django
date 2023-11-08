from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from materials.models import Material


# Create your views here.

class MaterialListView(ListView):
    model = Material
    template_name = 'materials/material_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title',
              'description',
              'image',
              'is_published',
              )
    success_url = '/materials/'

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title',
              'description',
              'image',
              'is_published',
              )
    # success_url = '/materials/view/' + self.object.pk

    def get_success_url(self):
        return reverse('materials:material_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'materials/material_delete.html'
    success_url = '/materials/'


def toggle_published(request, pk):
    material_item = get_object_or_404(Material, pk=pk)
    if material_item.is_published:
        material_item.is_published = False
    else:
        material_item.is_published = True

    material_item.save()

    return redirect(reverse('materials:material'))
