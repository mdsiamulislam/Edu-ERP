from .models import FeeCategory, Fee, Payment
from django.contrib import admin

admin.site.register(FeeCategory)
admin.site.register(Fee)
admin.site.register(Payment)
