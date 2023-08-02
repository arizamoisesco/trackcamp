from django import forms

class RegisterForm(forms.Form):
    hours_total_number = forms.IntegerField(label="Número Total de horas del curso", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Horas totales de la formación'}))
    hourly_intensity = forms.IntegerField(label="Intensidad horaria semanal", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Total de horas a la semana'}))