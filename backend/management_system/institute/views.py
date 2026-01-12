from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as Status

from .models import InstituteInfo
from .serializers import InstituteInfoSerializer

class InstituteInfoView(APIView):
    def get(self, request):
        institute_info = InstituteInfo.objects.first()
        serializer = InstituteInfoSerializer(institute_info)
        return Response(serializer.data, status=Status.HTTP_200_OK)
    
    def post(self, request):
        serializer = InstituteInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=Status.HTTP_201_CREATED)
        return Response(serializer.errors, status=Status.HTTP_400_BAD_REQUEST)
    
