from django.urls import path
from .views import PDFToAudioView

urlpatterns = [
    path('convert/', PDFToAudioView.as_view(), name='convert-pdf-audio'),
]