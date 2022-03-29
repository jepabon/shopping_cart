from django.db import models

from apps.order.models import Order

class Shipment(models.Model):
    STATUS_SHIPMENT_CHOICES = (
        ('new', 'Nuevo',),
        ('sent', 'Enviado',),
        ('delivered', 'Entregado',),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Pedido')
    address = models.CharField(max_length=255, null=True, blank=False, verbose_name='Dirección')
    status = models.CharField(max_length=50, default=STATUS_SHIPMENT_CHOICES[0][0], choices=STATUS_SHIPMENT_CHOICES, verbose_name='Estatus')

    def __str__(self):
        return "Envío #{}".format(self.id)
