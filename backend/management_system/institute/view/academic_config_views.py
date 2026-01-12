from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as Status

from ..models import AcademicConfig
from ..serializers import AcademicConfigSerializer

class AcademicConfigView(APIView):
    def get(self, request):
        academic_configs = AcademicConfig.objects.all()
        if not academic_configs.exists():
            return Response({"detail": "No academic configurations found."}, status=Status.HTTP_404_NOT_FOUND)
        serializer = AcademicConfigSerializer(academic_configs, many=True)
        return Response(serializer.data, status=Status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AcademicConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=Status.HTTP_201_CREATED)
        return Response(serializer.errors, status=Status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        academic_configs_id = request.data.get("id", None)
        if academic_configs_id is None:
            return Response({"detail": "ID is required to delete an academic configuration."}, status=Status.HTTP_400_BAD_REQUEST)
        try:
            academic_config = AcademicConfig.objects.get(id=academic_configs_id)
            academic_config.delete()
            return Response({"detail": "Academic configuration deleted successfully."}, status=Status.HTTP_200_OK)
        except AcademicConfig.DoesNotExist:
            return Response({"detail": "Academic configuration not found."}, status=Status.HTTP_404_NOT_FOUND)