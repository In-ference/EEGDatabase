from rest_framework import serializers
from .models import Metadata, Measure, Session, Classes, Trial, Channel, TimeSerie

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ['montage', 'createdDate', 'createdBy', 'protocol', 'samplingRate', 'samplingRateUnit', 'numberOfChannels', 'numberOfClasses']