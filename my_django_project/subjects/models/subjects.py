from django.db import models
from departments.models import Departments

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.discription}'