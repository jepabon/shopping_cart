from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.product.api.resources import ProductViewSet
from apps.order.api.resources import OrderViewSet
from apps.payment.api.resources import PaymentViewSet

router = SimpleRouter()
router.register(r'products', viewset=ProductViewSet)
router.register(r'orders', viewset=OrderViewSet)
router.register(r'payments', viewset=PaymentViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
