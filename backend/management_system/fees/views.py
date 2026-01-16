from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Fee, Payment
from .serializers import FeesTypeSerializer , FeePaymentSerializer


# Create your views here.
class FeesTypeListView(APIView):
    def get(self, request):
        fees_types = Fee.objects.all()
        serializer = FeesTypeSerializer(fees_types, many=True)
        return Response(serializer.data)
    
class FeePaymentListView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = FeePaymentSerializer(payments, many=True)
        return Response(serializer.data)
    

class FeePaymentView(APIView):
    def get(self, request, id):
        
        try:
            student_id = id
            payment = Payment.objects.filter(student=student_id)
            serializer = FeePaymentSerializer(payment, many=True)
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=404)