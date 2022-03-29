from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import redirect


from apps.base.decorators import is_client
from apps.base.utils import sent_email

from .forms import ShipmentForm
from .models  import Shipment

@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ShipmentCreateView(CreateView):
    form_class = ShipmentForm
    model = Shipment
    success_url = reverse_lazy('shipment:list')


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ShipmentUpdateView(UpdateView):
    form_class = ShipmentForm
    model = Shipment
    success_url = reverse_lazy('shipment:list')


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ShipmentDeleteView(DeleteView):
    form_class = ShipmentForm
    model = Shipment
    success_url = reverse_lazy('shipment:list')


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ShipmentListView(ListView):
    model = Shipment


@method_decorator(login_required, name='dispatch')
@method_decorator(is_client, name='dispatch')
class ShipmentSentView(TemplateView):
    template_name = "shipment/sent.html"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("shipment:list")

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        shipment = Shipment.objects.filter(id=pk).first()
        if shipment is not None:
            shipment.status = 'sent'
            shipment.save()

            subject = "{} ha sido enviado".format(str(shipment.order))
            content = "El pedido ya se encuentra enviado, por favor estar atento."

            if shipment.order.created_by.email:
                sent_email(subject, shipment.order.created_by.email, content)

        return redirect(self.get_success_url())
