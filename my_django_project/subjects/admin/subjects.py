from django.contrib import admin

from subjects.models import Subjects

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    pass