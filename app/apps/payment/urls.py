from django.urls import path

from .views import ProcessPayment

app_name = 'payment'

urlpatterns = [
    path('process_payment/', ProcessPayment.as_view(), name='process_payment'),
]
