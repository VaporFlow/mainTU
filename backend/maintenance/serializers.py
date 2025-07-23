from rest_framework import serializers
from .models import TaskAssignment

class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = ["id", "name", "scheduled_date", "created_at"]
