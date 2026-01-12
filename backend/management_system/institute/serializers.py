from rest_framework import serializers
from .models import InstituteInfo, AcademicConfig, Class, InstituteSettings


class InstituteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteInfo
        fields = '__all__'

class AcademicConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicConfig
        fields = '__all__'