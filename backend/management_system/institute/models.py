from django.db import models



# Institute Info Models

class InstituteInfo(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    logo = models.ImageField(upload_to='institute_logos/', null=True, blank=True)
    established_date = models.DateField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    

# Academic Config Models
class AcademicConfig(models.Model):
    current_academic_year = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)


    def __str__(self):
        return f"Academic Config for {self.current_academic_year}"
    

# Class Models
class Class(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
# Institute Settings Models
class InstituteSettings(models.Model):
    allow_student_registration = models.BooleanField(default=True)
    max_students_per_class = models.IntegerField(default=30)
    enable_notifications = models.BooleanField(default=True)


    def __str__(self):
        return "Institute Settings"