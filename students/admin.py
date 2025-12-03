from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_name', 'parents_name', 'guardian')
    search_fields = ('name', 'class_name', 'parents_name')
