from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=100)
    head_of_the_departmenton = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.head_of_the_departmenton}'