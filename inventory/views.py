from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from inventory.models import Category, Item
from inventory.forms import CreateItemForm


class CategoryListView(generic.ListView):
    '''ListView for showing different categories'''
    model = Category
    template_name = 'inventory/index.html'


class CategoryCreateView(generic.edit.CreateView):
    '''View for creating new category'''
    model = Category
    fields = ['name']
    success_url = reverse_lazy('inventory:index')


class CategoryItemsListView(generic.ListView):
    '''List the items in a category'''
    model = Category

    def get_queryset(self) -> QuerySet[Any]:
        return get_object_or_404(Category, pk=self.kwargs['pk']).items.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['category_name'] = get_object_or_404(
            Category, pk=self.kwargs['pk']).name
        context['category_id'] = self.kwargs['pk']
        return context


class CategoryDeleteView(generic.edit.DeleteView):
    '''Generic view for deleting category'''
    model = Category
    success_url = reverse_lazy('inventory:index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs['pk']
        return context


class ItemCreateView(generic.edit.CreateView):
    '''Generic view for creating new item'''
    model = Item
    form_class = CreateItemForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.category = get_object_or_404(
            Category, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self) -> str:
        # return super().get_success_url()
        return reverse_lazy('inventory:category-items', args=[self.kwargs['pk']])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs['pk']
        return context


class ItemDeleteView(generic.edit.DeleteView):
    '''Generic view for deleting an item'''
    model = Item
    template_name = 'inventory/category_confirm_delete.html'

    def get_success_url(self) -> str:
        # return super().get_success_url()
        return reverse_lazy(
            'inventory:category-items', args=[self.kwargs['cat_id']])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs['cat_id']
        return context


class ItemEditView(generic.edit.UpdateView):
    '''Generic view for updating item'''
    model = Item
    form_class = CreateItemForm

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs['cat_id']
        context['edit'] = True
        return context

    def get_success_url(self) -> str:
        # return super().get_success_url()
        return reverse_lazy(
            'inventory:category-items', args=[self.kwargs['cat_id']])