from django.contrib import admin

from teachers.models import Load

@admin.register(Load)
class LoadsAdmin(admin.ModelAdmin):
    pass