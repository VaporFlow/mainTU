from __future__ import annotations

import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import TestCase, override_settings
from parts.models import UploadedCSV


class CleanupCSVCommandTests(TestCase):
    """Tests for the cleanup_csvs management command."""

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_cleanup_removes_old_entries(self) -> None:
        for i in range(7):
            UploadedCSV.objects.create(
                file=SimpleUploadedFile(f"test{i}.csv", b"a,b,c"),
                original_name=f"test{i}.csv",
            )
        self.assertEqual(UploadedCSV.objects.count(), 7)

        call_command("cleanup_csvs")

        remaining = UploadedCSV.objects.order_by("-uploaded_at")
        self.assertEqual(remaining.count(), 5)
        newest = list(UploadedCSV.objects.order_by("-uploaded_at").values_list("original_name", flat=True))
        expected = [f"test{i}.csv" for i in reversed(range(2, 7))]
        self.assertEqual(newest[:5], expected)
