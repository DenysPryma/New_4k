from django.contrib import admin

from teachers.models import Teachers

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    pass