"""Basic API availability tests for the parts app."""

import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import TestCase, override_settings
from parts.models import UploadedCSV


class ApiSmokeTests(TestCase):
    """Ensure main API endpoints respond with HTTP 200."""

    def test_parts_endpoint(self) -> None:
        """`/api/parts/` should return HTTP 200."""

        response = self.client.get("/api/parts/")
        self.assertEqual(response.status_code, 200)

    def test_taskings_endpoint(self) -> None:
        """`/api/taskings/` should return HTTP 200."""

        response = self.client.get("/api/taskings/")
        self.assertEqual(response.status_code, 200)


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
        newest = list(
            UploadedCSV.objects.order_by("-uploaded_at").values_list(
                "original_name", flat=True
            )
        )
        expected = [f"test{i}.csv" for i in reversed(range(2, 7))]
        self.assertEqual(newest[:5], expected)


class UploadedCSVViewSetTests(TestCase):
    """Test the UploadedCSVViewSet filtering logic."""

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_list_returns_latest_five(self) -> None:
        for i in range(7):
            UploadedCSV.objects.create(
                file=SimpleUploadedFile(f"file{i}.csv", b"a,b,c"),
                original_name=f"file{i}.csv",
            )

        response = self.client.get("/api/parts/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 5)
        names = [row["original_name"] for row in data]
        expected = [f"file{i}.csv" for i in reversed(range(2, 7))]
        self.assertEqual(names, expected)

