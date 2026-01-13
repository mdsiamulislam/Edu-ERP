from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Admission
from ..serializers import AdmissionSerializer


class AdmissionListView(APIView):
    def get(self, request):
        admissions = Admission.objects.all()
        serializer = AdmissionSerializer(admissions, many=True)
        if not serializer.data:
            return Response({"message": "No admissions found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = AdmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
