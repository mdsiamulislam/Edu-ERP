
from django.contrib import admin
from django.urls import path, include
from .views import FeesTypeListView, FeePaymentListView , FeePaymentView

urlpatterns = [
    path('fees-types/', FeesTypeListView.as_view(), name='fees-type-list'),
    path('fee-payments/', FeePaymentListView.as_view(), name='fee-payment-list'),
    path('payment/<int:id>/',FeePaymentView.as_view(), name='fee-pay'),
]
