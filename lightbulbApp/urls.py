from django.urls import path
from . import views

urlpatterns = [
    path('', views.sampleView, name='sample'),
]