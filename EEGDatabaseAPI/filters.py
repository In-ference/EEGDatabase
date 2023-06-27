import django_filters
from .models import TimeSerie

class TimeSerieFilter(django_filters.FilterSet):
    time = django_filters.RangeFilter(field_name='time')
    subject_id = django_filters.CharFilter(lookup_expr='exact')
    trial = django_filters.CharFilter(lookup_expr='exact')
    class_id = django_filters.CharFilter(lookup_expr='exact')
    session = django_filters.CharFilter(lookup_expr='exact')
    run = django_filters.CharFilter(lookup_expr='exact')
    channel = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = TimeSerie
        fields = ['time','subject_id', 'trial', 'class_id', 'session', 'run', 'channel']