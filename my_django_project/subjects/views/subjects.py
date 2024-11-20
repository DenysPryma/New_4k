from rest_framework import generics

from subjects.models import Subjects
from subjects.serializers import SubjectsSerializer

class SubjectsList(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

class SubjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer