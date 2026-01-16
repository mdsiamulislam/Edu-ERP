from rest_framework import serializers
from admissions.models import Admission as Student, Class as SchoolClass
from institute.models import AcademicConfig

# ১. সবার আগে থাকবে কনফিগ সিরিয়ালাইজার
class AcademicConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicConfig
        fields = ['current_academic_year', 'start_date', 'end_date', 'is_current']  

# ২. তারপর ক্লাস সিরিয়ালাইজার (এর ভেতরে কনফিগ থাকবে)
class SchoolClassSerializer(serializers.ModelSerializer):
    # এখানে config ফিল্ডের নাম আপনার Class মডেলে যা আছে সেটা দিবেন (ধরি academic_config)
    academic_config = AcademicConfigSerializer(read_only=True) 

    class Meta:
        model = SchoolClass
        fields = ['name', 'academic_config'] # আপনার ক্লাসের ফিল্ডগুলো এখানে দিন

# ৩. সবশেষে স্টুডেন্ট সিরিয়ালাইজার
class StudentSerializer(serializers.ModelSerializer):
    applied_class = SchoolClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'applied_class']