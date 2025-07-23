from rest_framework import viewsets
from .models import UploadedCSV
from .serializers import UploadedCSVSerializer

class UploadedCSVViewSet(viewsets.ModelViewSet):
    """API view set for uploaded CSVs."""

    serializer_class = UploadedCSVSerializer

    def get_queryset(self):
        """Return only the five newest records."""

        return UploadedCSV.objects.order_by("-uploaded_at")[:5]
