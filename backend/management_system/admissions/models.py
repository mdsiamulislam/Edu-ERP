from django.db import models
from institute.models import Class, AcademicConfig

# Create your models here.

class Admission(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    guardian_name = models.CharField(max_length=50)
    guardian_phone = models.CharField(max_length=15)
    application_date = models.DateField(auto_now_add=True)

    # Getting the class from institute models
    applied_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicConfig, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    registration_number = models.IntegerField(auto_created=True, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
