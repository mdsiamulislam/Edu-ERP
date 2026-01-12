from rest_framework import serializers
from .models import Fee, Payment

class FeesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'


class FeePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'