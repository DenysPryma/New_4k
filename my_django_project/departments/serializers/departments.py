from rest_framework import serializers

from departments.models import Departments


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['name', 'head_of_the_departmenton']