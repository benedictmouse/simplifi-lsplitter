# splitter/serializers.py
from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        ext = value.name.rsplit('.', 1)[-1].lower()
        if ext not in ['ods', 'xlsx', 'xls']:
            raise serializers.ValidationError("Only .ods, .xlsx, or .xls files are supported.")
        return value