from rest_framework import serializers
from .models import InstituteInfo


class InstituteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteInfo
        fields = '__all__'