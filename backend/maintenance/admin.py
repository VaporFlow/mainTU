from django.contrib import admin
from .models import TaskAssignment

@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ["name", "scheduled_date", "created_at"]
