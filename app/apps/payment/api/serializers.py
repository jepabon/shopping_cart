from ..models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    creation_date = serializers.ReadOnlyField()
    created_by = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
