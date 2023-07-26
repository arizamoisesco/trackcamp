from django import forms

class RegisterForm(forms.Form):
    hours_total_number = forms.IntegerField(label="Número Total de horas")
    hourly_intensity = forms.IntegerField(label="Intensidad horaria")