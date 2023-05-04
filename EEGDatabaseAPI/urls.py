from django.urls import path
from . import views

urlpatterns = [
    path('metadata', views.MetadataView.as_view()),
    path('measure', views.MeasureView.as_view()),
    path('session', views.SessionView.as_view()),
    path('classes', views.ClassesView.as_view()),
]