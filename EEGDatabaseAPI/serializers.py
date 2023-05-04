from rest_framework import serializers
from .models import Metadata, Measure, Session, Classes, Subject, Channel, TimeSerie

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

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_id', 'description']

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['channel_name']

class TimeSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSerie
        fields = ['time', 'value', 'subject_id', 'trial', 'session', 'run', 'channel']