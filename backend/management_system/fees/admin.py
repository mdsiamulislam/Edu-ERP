from django.contrib import admin
from .models import  FeesType, FeeComponent, FeePlan, StudentFeeRecord, FeePayment, FeesFor , MakeFees

# Register your models here.
admin.site.register(FeesType)
admin.site.register(FeeComponent)
admin.site.register(FeePlan)
admin.site.register(StudentFeeRecord)
admin.site.register(FeePayment)

# My Style #
admin.site.register(FeesFor)
admin.site.register(MakeFees)