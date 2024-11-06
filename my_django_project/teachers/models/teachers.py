from django.db import models
from departments.models import Departments

class Teachers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    position = models.CharField(max_length=35)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'