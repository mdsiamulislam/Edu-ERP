from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as Status

from .models import InstituteInfo
from .serializers import InstituteInfoSerializer

class InstituteInfoView(APIView):
    def get(self, request):
        institute_info = InstituteInfo.objects.first()
        if not institute_info:
            return Response({"detail": "Institute information not found."}, status=Status.HTTP_404_NOT_FOUND)
        
        serializer = InstituteInfoSerializer(institute_info)
        return Response(serializer.data, status=Status.HTTP_200_OK)
    
    def post(self, request):
        serializer = InstituteInfoSerializer(data=request.data)
        if serializer.is_valid() and not InstituteInfo.objects.exists():
            serializer.save()
            return Response(serializer.data, status=Status.HTTP_201_CREATED)
        return Response(serializer.errors, status=Status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        institute_info = InstituteInfo.objects.first()
        serializer = InstituteInfoSerializer(institute_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=Status.HTTP_200_OK)
        return Response(serializer.errors, status=Status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        is_confirm = request.data.get("confirm", False)
        if not is_confirm:
            return Response({"error": "Please confirm deletion by setting 'confirm' to true."}, status=Status.HTTP_400_BAD_REQUEST)
        institute_info = InstituteInfo.objects.first()
        institute_info.delete()
        return Response(status=Status.HTTP_204_NO_CONTENT)  
    


