from rest_framework import viewsets
from .models import UploadedCSV
from .serializers import UploadedCSVSerializer

class UploadedCSVViewSet(viewsets.ModelViewSet):
    queryset = UploadedCSV.objects.all().order_by("-uploaded_at")[:5]
    serializer_class = UploadedCSVSerializer
