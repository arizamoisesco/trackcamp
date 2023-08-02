from django import forms
from django.forms import widgets
from .models import Cohorte

class RegisterForm(forms.Form):
    #name_cohorte = forms.CharField(max_length=25)
    #name_trainer = forms.CharField(max_length=25)
    #name_cotrainer = forms.CharField(max_length=25)
    duration_cohorte = forms.IntegerField(label="Duranción de la cohorte", widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad de meses totales'}))
    start_cohorte = forms.DateField(label="Fecha de inicio de cohorte", widget=forms.widgets.DateInput(attrs={'class':'form-control','type': 'date'}))