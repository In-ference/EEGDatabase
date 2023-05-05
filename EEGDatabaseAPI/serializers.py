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
    #class Meta:
    #    model = TimeSerie
    #    fields = ['time', 'value', 'subject_id', 'trial', 'session', 'run', 'channel']
    time = serializers.ListField(child=serializers.FloatField())
    value = serializers.ListField(child=serializers.FloatField())
    subject_id = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    trial = serializers.IntegerField()
    class_id = serializers.PrimaryKeyRelatedField(queryset=Classes.objects.all())
    session = serializers.PrimaryKeyRelatedField(queryset=Session.objects.all())
    run = serializers.IntegerField()
    channel = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all())

    def create(self, validated_data):
        data_list = []
        for i in range(len(validated_data['value'])):
            data_list.append(TimeSerie(
                time=validated_data['time'][i],
                value=validated_data['value'][i],
                subject_id=validated_data['subject_id'],
                trial=validated_data['trial'],
                class_id=validated_data['class_id'],
                session=validated_data['session'],
                run=validated_data['run'],
                channel=validated_data['channel']
            ))
        TimeSerie.objects.bulk_create(data_list)
        return validated_data
    
    class Meta:
        model = TimeSerie
        fields = "__all__"
