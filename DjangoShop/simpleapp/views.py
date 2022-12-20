from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Product
from .filters import ProductFilter
from .forms import ProductForm


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'flatpages/products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'flatpages/product.html'
    context_object_name = 'product'

#Можно создать представление с помощью функции, а не класса
#def create_product(request):
    #form = ProductForm()
    #if request.method == 'POST':
        #form = ProductForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return HttpResponseRedirect('/products/')
    #return render(request, 'flatpages/product_edit.html', {'form': form})


class ProductCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_product',)
    form_class = ProductForm
    model = Product
    template_name = 'flatpages/product_edit.html'


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_product',)
    form_class = ProductForm
    model = Product
    template_name = 'flatpages/product_edit.html'


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_product',)
    model = Product
    template_name = 'flatpages/product_delete.html'
    success_url = reverse_lazy('product_list')

