from rest_framework import serializers
from .models import Admission


class AdmissionSerializer(serializers.ModelSerializer):
    # GET response এর জন্য
    applied_class_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Admission
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'phone',
            'address',
            'guardian_name',
            'guardian_phone',
            'application_date',
            'is_approved',
            'registration_number',
            'applied_class',       # POST/PUT/PATCH এর জন্য ID
            'applied_class_name',  # GET response এ class name দেখাবে
        ]

    # GET response customization
    def get_applied_class_name(self, obj):
        return {
            'id': obj.applied_class.id,
            'name': obj.applied_class.name
        }
