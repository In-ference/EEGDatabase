from django.db import models
from timescale.db.models.models import TimescaleModel

# Create your models here.
class Metadata(models.Model):
    montage = models.CharField(primary_key=True, unique=True, max_length=255)
    createdDate = models.CharField(max_length=100)
    createdBy = models.CharField(max_length=255)
    protocol = models.CharField(max_length=255)
    samplingRate = models.DecimalField(max_digits=10, decimal_places=2)
    samplingRateUnit = models.CharField(max_length=255)
    numberOfChannels = models.IntegerField(null=True, blank=True)
    numberOfClasses = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.montage}"

class Measure(models.Model):
    type = models.CharField(primary_key=True, unique=True, max_length=255)
    metadata = models.ForeignKey(Metadata, on_delete=models.CASCADE)
    description = models.CharField(max_length=2**16, null=True, blank=True)

    def __str__(self):
        return f"{self.type}"

class Session(models.Model):
    session_name = models.CharField(default='Training', primary_key=True, unique=True, max_length=255)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    description = models.CharField(max_length=2**16, null=True, blank=True)

    def __str__(self):
        return f"{self.session_name}"

class Classes(models.Model):
    class_id = models.IntegerField(primary_key=True, unique=True, default=1)
    label = models.CharField(max_length=255)
    description = models.CharField(max_length=2**16)

    def __str__(self):
        return f"{self.class_id} {self.label}"
class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True, unique=True)
    description = models.CharField(max_length=2**16)

    def __str__(self):
        return f"{self.subject_id}"

class Channel(models.Model):
    channel_name = models.CharField(primary_key=True, unique=True, max_length=255)

    def __str__(self):
        return f"{self.channel_name}"

class TimeSerie(TimescaleModel):
    time = models.FloatField()
    value = models.FloatField()
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    trial = models.IntegerField(null=True, blank=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, to_field='class_id')
    session = models.ForeignKey(Session , on_delete=models.CASCADE, null=True, blank=True)
    run = models.IntegerField(default=0)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.time} {self.value} {self.trial} {self.channel}"