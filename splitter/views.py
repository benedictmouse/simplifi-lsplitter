# splitter/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .serializers import FileUploadSerializer
from .utils import split_by_sku

class SKUSplitterView(APIView):
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        uploaded_file = serializer.validated_data['file']

        try:
            zip_buffer = split_by_sku(uploaded_file, uploaded_file.name)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Processing failed: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response = HttpResponse(
            zip_buffer.read(),
            content_type='application/zip'
        )
        response['Content-Disposition'] = 'attachment; filename="sku_split_files.zip"'
        return response