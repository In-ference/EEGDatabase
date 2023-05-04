from django.urls import path
from . import views

urlpatterns = [
    path('metadata', views.MetadataView.as_view()),
    path('measure', views.MeasureView.as_view()),
    path('session', views.SessionView.as_view()),
    path('classes', views.ClassesView.as_view()),
    path('subject', views.SubjectView.as_view()),
    path('channel', views.ChannelView.as_view()),
    path('timeserie', views.TimeSerieView.as_view()),
]