"""Parts models."""

from __future__ import annotations

import os
from django.db import models
from django.utils import timezone


def upload_to(instance: "UploadedCSV", filename: str) -> str:
    """Return path for uploaded CSV files with a timestamped name.

    The original filename is stored on the instance and a UTC timestamp is
    inserted before the extension. Files are organised under ``csv/YYYY/MM/DD``
    to avoid cluttering a single directory.
    """

    instance.original_name = filename
    now = timezone.now()
    base, ext = os.path.splitext(filename)
    timestamp = now.strftime("%Y%m%d%H%M%S")
    dated_path = os.path.join("csv", now.strftime("%Y"), now.strftime("%m"), now.strftime("%d"))
    return os.path.join(dated_path, f"{base}_{timestamp}{ext}")

class UploadedCSV(models.Model):
    """CSV file uploaded by users."""

    file = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(default=timezone.now)
    original_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.original_name

