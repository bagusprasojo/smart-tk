from django.contrib import admin

from .models import Mutabaah


@admin.register(Mutabaah)
class MutabaahAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'date')
    list_filter = ('date', 'teacher')
    search_fields = ('student__name', 'teacher__username')
