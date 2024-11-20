from rest_framework import generics

from teachers.models import Load
from teachers.serializers import LoadSerializer

class loadList(generics.ListCreateAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer

class LoadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer