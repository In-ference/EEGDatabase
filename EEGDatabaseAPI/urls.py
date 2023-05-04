from django.urls import path
from . import views

urlpatterns = [
    path('metadata', views.MetadataList.as_view()),
]