from django.urls import path
from . import views

app_name = 'cohorteTimer'

urlpatterns = [
    path('', views.record_time, name='record-time'),
]