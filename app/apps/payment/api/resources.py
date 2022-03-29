from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone

from ..models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    order_by = ['id']

    def list(self, request, version='v1'):
        response = {}

        queryset = self.get_queryset()
        queryset = queryset.filter(paymentorder__isnull=True)

        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        response["results"] = serializer.data
        response["method_payments"] = Payment.METHOD_PAYMENT_CHOICES

        return Response(response)

    @action(methods=['get'], detail=False, name="create_payment")
    def create_payment(self, request):
        payment = Payment()
        payment.creation_date = timezone.now()
        payment.created_by = self.request.user
        payment.save()

        return Response({'status': 'Payment created'})
