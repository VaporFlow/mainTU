from django.db.models import QuerySet
from rest_framework import viewsets

from .models import UploadedCSV
from .serializers import UploadedCSVSerializer

class UploadedCSVViewSet(viewsets.ModelViewSet):
    """API view set for uploaded CSVs."""

    serializer_class = UploadedCSVSerializer

    def get_queryset(self) -> QuerySet[UploadedCSV]:
        """Return the latest five uploaded CSV records."""

        return UploadedCSV.objects.order_by("-uploaded_at")[:5]
