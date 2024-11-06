from django.contrib import admin

from departments.models import Departments

@admin.register(Departments)
class DepartmetsAdmin(admin.ModelAdmin):
    pass