from django.db import models
from django.utils import timezone

class UploadedCSV(models.Model):
    """CSV file uploaded by users."""

    file = models.FileField(upload_to="csv/%Y/%m/%d")
    uploaded_at = models.DateTimeField(default=timezone.now)
    original_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.original_name

