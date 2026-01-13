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

class ClassSerializer(serializers.ModelSerializer):
    academic_year = serializers.SerializerMethodField()   
    class Meta:
        model = Class
        fields = [
            'id',
            'name',
            'academic_year',
            'academic_config',
            'is_active',
        ]

    def get_academic_year(self, obj):
        return{
            'id': obj.academic_config.id,
            'name': obj.academic_config.current_academic_year,
        }