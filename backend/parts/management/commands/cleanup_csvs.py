from __future__ import annotations

from django.core.management.base import BaseCommand
from parts.models import UploadedCSV

class Command(BaseCommand):
    """Delete uploaded CSV entries beyond the latest five."""

    help = "Remove old UploadedCSV records, keeping only the latest five."

    def handle(self, *args, **options):
        latest_ids = list(
            UploadedCSV.objects.order_by("-uploaded_at").values_list("id", flat=True)[:5]
        )
        old_entries = UploadedCSV.objects.exclude(id__in=latest_ids)
        count = 0
        for obj in old_entries:
            if obj.file:
                obj.file.delete(save=False)
            obj.delete()
            count += 1
        self.stdout.write(self.style.SUCCESS(f"Deleted {count} old CSV entries."))

