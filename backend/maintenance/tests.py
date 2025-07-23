"""Basic API availability tests for the maintenance app."""

from django.test import TestCase


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

