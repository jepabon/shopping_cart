from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


from apps.base.decorators import is_client

from .forms import ProductForm
from .models  import Product

@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ProductCreateView(CreateView):
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('product:list')


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ProductUpdateView(UpdateView):
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('product:list')


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ProductDeleteView(DeleteView):
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('product:list')


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ProductListView(ListView):
    model = Product
