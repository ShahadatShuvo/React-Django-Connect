from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id', 'stuname', 'email'
    ]


admin.site.register(Student, StudentAdmin)
