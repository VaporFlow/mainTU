from django.db import models
from django.utils import timezone

class TaskAssignment(models.Model):
    """Maintenance task derived from forecast."""

    name = models.CharField(max_length=255)
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name

