from django.urls import path
from . import views

app_name = 'classtimeConversion'

urlpatterns = [
    path('', views.months_calculation, name='months-calculation')
]