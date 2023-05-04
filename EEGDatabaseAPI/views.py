from django.shortcuts import render
from .models import Metadata, Measure, Session, Classes, Trial, Channel, TimeSerie
from .serializers import MetadataSerializer, MeasureSerializer, SessionSerializer, ClassesSerializer
from rest_framework import generics
# Create your views here.

class MetadataView(generics.ListCreateAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

class MeasureView(generics.ListCreateAPIView):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer

class SessionView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ClassesView(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer