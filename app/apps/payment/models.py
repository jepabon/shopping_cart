from pyexpat import model
from django.db import models
from apps.order.models import Order
from django.contrib.auth.models import User


class Payment(models.Model):
    METHOD_PAYMENT_CHOICES = (
        ('cash', 'Efectivo',),
        ('check', 'Cheque',),
        ('debit_card', 'Tarjeta Débito',),
        ('credit_card', 'Tarjeta de Crédito',),
        ('transfer', 'Transferencia',),
    )

    method_payment = models.CharField(max_length=50, choices=METHOD_PAYMENT_CHOICES, default=METHOD_PAYMENT_CHOICES[0][0], null=True, blank=False, verbose_name="Método de Pago")
    value = models.FloatField(null=True, blank=False, verbose_name="Valor")
    creation_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Fecha de Creación")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Creado Por")


class PaymentOrder(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Payment")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Order")
