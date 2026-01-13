from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as Status

from ..models import Class
from ..serializers import ClassSerializer

class ClassView(APIView):
    def get(self, request):
        classes = Class.objects.all()
        if not classes.exists():
            return Response({"detail": "No classes found."}, status=Status.HTTP_404_NOT_FOUND)
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=Status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cusetom_response = {"detail": "Class created successfully.", "response": serializer.data}
            return Response(cusetom_response, status=Status.HTTP_201_CREATED)
        return Response(serializer.errors, status=Status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        class_id = request.data.get("id", None)
        if class_id is None:
            return Response({"detail": "ID is required to update a class."}, status=Status.HTTP_400_BAD_REQUEST)
        try:
            class_instance = Class.objects.get(id=class_id)
            serializer = ClassSerializer(class_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=Status.HTTP_200_OK)
            return Response(serializer.errors, status=Status.HTTP_400_BAD_REQUEST)
        except Class.DoesNotExist:
            return Response({"detail": "Class not found."}, status=Status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request):
        class_id = request.data.get("id", None)
        if class_id is None:
            return Response({"detail": "ID is required to delete a class."}, status=Status.HTTP_400_BAD_REQUEST)
        try:
            class_instance = Class.objects.get(id=class_id)
            class_instance.delete()
            return Response({"detail": "Class deleted successfully."}, status=Status.HTTP_200_OK)
        except Class.DoesNotExist:
            return Response({"detail": "Class not found."}, status=Status.HTTP_404_NOT_FOUND)