from rest_framework.views import APIView
from rest_framework.response import Response
from .serialization import StudentSerializer
from admissions.models import Admission as Student


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)