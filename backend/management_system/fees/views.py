from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Fee, Payment


# Create your views here.
class FeesTypeListView(APIView):
    def get(self, request):
        fees_types = Fee.objects.all()
        data = [{'id': ft.id, 'name': ft.name, 'amount': ft.amount} for ft in fees_types]
        return Response(data)
    
class FeePaymentListView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        data = [{'id': p.id, 'student': {
            'id': p.student.id, 'name': p.student.first_name
        }, 'fee': p.fee.id, 'amount_paid': p.amount_paid} for p in payments]
        return Response(data)
