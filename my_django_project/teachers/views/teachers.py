from rest_framework import generics

from teachers.models import Teachers
from teachers.serializers import TeachersSerializer

class TeachersList(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

class TeachersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer