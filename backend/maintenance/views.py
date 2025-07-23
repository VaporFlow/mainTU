from rest_framework import viewsets
from .models import TaskAssignment
from .serializers import TaskAssignmentSerializer

class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all().order_by("scheduled_date")
    serializer_class = TaskAssignmentSerializer
