from django.shortcuts import render
from .models import Metadata, Measure, Session, Classes, Trial, Channel, TimeSerie
from .serializers import MetadataSerializer
from rest_framework import generics
# Create your views here.

class MetadataList(generics.ListCreateAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer