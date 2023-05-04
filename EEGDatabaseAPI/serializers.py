from rest_framework import serializers
from .models import Metadata, Measure, Session, Classes, Trial, Channel, TimeSerie

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ['montage', 'createdDate', 'createdBy', 'protocol', 'samplingRate', 'samplingRateUnit', 'numberOfChannels', 'numberOfClasses']

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['type', 'metadata', 'description']

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['session_name', 'measure', 'description']

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['class_id', 'label', 'description']