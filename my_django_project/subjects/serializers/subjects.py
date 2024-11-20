from rest_framework import serializers

from subjects.models import Subjects


class SubjectsSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(queryset=Subjects.objects.all(), required=False)
    
    class Meta:
        model = Subjects
        fields = ['name', 'discription', 'department_id']