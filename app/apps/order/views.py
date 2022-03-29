from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.base.decorators import is_client

from .forms import OrderForm
from .models  import Order


@method_decorator(login_required, name='dispatch')
class OrderDetail(TemplateView):
    template_name = "order_detail.html"



@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class OrderCreateView(CreateView):
    form_class = OrderForm
    model = Order
    success_url = reverse_lazy('order:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.created_by is None:
            self.object.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class OrderUpdateView(UpdateView):
    form_class = OrderForm
    model = Order
    success_url = reverse_lazy('order:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.created_by is None:
            self.object.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class OrderDeleteView(DeleteView):
    form_class = OrderForm
    model = Order
    success_url = reverse_lazy('order:list')


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class OrderListView(ListView):
    model = Order
