from rest_framework import serializers

from teachers.models import Load


class LoadSerializer(serializers.ModelSerializer):
    subject_id = serializers.PrimaryKeyRelatedField(queryset=Load.objects.all(), required=False)
    class Meta:
        model = Load
        fields = ['lecture_hours', 'practical_hours', 'subject_id']