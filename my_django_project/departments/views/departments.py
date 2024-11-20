from rest_framework import generics


from departments.models import Departments
from departments.serializers import DepartmentsSerializer

class DepartmentsList(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class DepartmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer