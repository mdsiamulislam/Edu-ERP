from django.db import models
from admissions.models import Admission as Student

# Fee Category Models
class FeeCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name
    
# Fee Models
class Fee(models.Model):
    category = models.ForeignKey(FeeCategory, on_delete=models.CASCADE, related_name='fees')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    accept_date = models.DateField()
    due_date = models.DateField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.category.name} - {self.amount}"
    
# Payment Models
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE, related_name='payments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    transection_date = models.DateField()
    payment_date = models.DateField(auto_now_add=True)
    receipt_number = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return f"Payment {self.receipt_number} - {self.amount_paid}"