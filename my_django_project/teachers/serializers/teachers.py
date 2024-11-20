from rest_framework import serializers

from teachers.models import Teachers


class TeachersSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(queryset=Teachers.objects.all(), required=False)
    
    class Meta:
        model = Teachers
        fields = ['first_name', 'last_name', 'department_id', 'position']