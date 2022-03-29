from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from apps.order.models import Order

from apps.payment.models import PaymentOrder


@method_decorator(login_required, name='dispatch')
class ProcessPayment(TemplateView):
    template_name = "process_payment.html"

    def get(self, *args, **kwargs):
        if self.request.user.order_set.exists():
            self.request.user.order_set.filter(status='new').update(status='confirmed')
        
        return super().get(*args, **kwargs)
    
    def post(self, *args, **kwargs):

        payments = json.loads(self.request.POST.get('payments', '[]'))
        payments = payments.get('results', [])
        orders = json.loads(self.request.POST.get('orders', '[]'))
        print("orders", orders)
        print("payments", payments)

        for _order in orders:
            order = _order.get('order', {})
            total = order.get('total', 0)
            if total <= 0:
                continue
            for payment in payments:
                if payment.get('value', 0) <= 0:
                    continue

                payment_order = PaymentOrder()
                payment_order.order_id = order.get('id')
                payment_order.payment_id = payment.get('id')
                payment_order.save()

                total -= payment.get('value', 0)

                if total <= 0:
                    order_db = Order.objects.filter(id=order.get('id')).first()
                    if order_db is not None:
                        order_db.status = 'paid'
                        order_db.save()
                    break

        return redirect(reverse_lazy('index'))
