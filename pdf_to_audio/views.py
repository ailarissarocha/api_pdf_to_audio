# pdf_to_audio/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PDFUploadSerializer
from .utils import pdf_to_audio
import os

class PDFToAudioView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PDFUploadSerializer(data=request.data)
        if serializer.is_valid():
            pdf_file = serializer.validated_data['file']
            input_path = os.path.join('tmp', pdf_file.name)
            output_path = os.path.join('tmp', pdf_file.name.replace('.pdf', '.mp3'))

            with open(input_path, 'wb') as f:
                for chunk in pdf_file.chunks():
                    f.write(chunk)
            
            pdf_to_audio(input_path, output_path)

            return Response({'audio_file': output_path}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)