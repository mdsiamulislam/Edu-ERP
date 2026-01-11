from django.db import models
from admissions.models import Admission as Student
from institute.models import AcademicConfig , Class

# Create your models here.

class FeesType(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class FeeComponent(models.Model):
    FEE_COMPONENT_CHOICES = [
        ('admission', 'Admission Fee'),
        ('january', 'January Fee'),
        ('february', 'February Fee'),
        ('mid_exam', 'Mid Exam'),
        ('final_exam', 'Final Exam'),
        ('test_exam', 'Test Exam'),
    ]
    
    EXAM_TYPE_CHOICES = [
        ('mid', 'Mid Exam'),
        ('final', 'Final Exam'),
        ('test', 'Test Exam'),
    ]
    
    fee_type = models.ForeignKey(FeesType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=FEE_COMPONENT_CHOICES)
    month = models.IntegerField(null=True, blank=True)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES, blank=True)

    def __str__(self):
        return f"{self.fee_type.name} Component"
    
class FeePlan(models.Model):
    academic_year = models.ForeignKey(AcademicConfig, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)
    fee_components = models.ManyToManyField(FeeComponent)
    name = models.CharField(max_length=100, default="Standard Fee Plan")
    def __str__(self):
        return self.name
    
class StudentFeeRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_plan = models.ForeignKey(FeePlan, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Fee Record for {self.student}"
    
class FeePayment(models.Model):
    student_fee_record = models.ForeignKey(StudentFeeRecord, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment of {self.amount_paid} on {self.payment_date}"



# My Style #
class FeesFor(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    assaigned_year = models.ForeignKey(AcademicConfig, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class MakeFees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    admission_fee = models.ForeignKey(FeesFor, on_delete=models.CASCADE)
    january_fee = models.ForeignKey(FeesFor, related_name='january_fee', on_delete=models.CASCADE)
    february_fee = models.ForeignKey(FeesFor, related_name='february_fee', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.fee_type.name} for month {self.month}"