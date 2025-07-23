from rest_framework import serializers
from .models import UploadedCSV

class UploadedCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedCSV
        fields = ["id", "original_name", "file", "uploaded_at"]
