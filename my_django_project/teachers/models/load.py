from django.db import models
from subjects.models import Subjects


class Load(models.Model):
    lecture_hours = models.FloatField()
    practical_hours  = models.FloatField()
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lecture_hours}'