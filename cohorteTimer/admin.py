from django.contrib import admin
from .models import Teacher, Program

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'position']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'creation_date', 'update_date']

