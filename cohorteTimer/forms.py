from django import forms

class RegisterForm(forms.Form):
    name_cohorte = forms.CharField(max_length=25)
    name_trainer = forms.CharField(max_length=25)
    name_cotrainer = forms.CharField(max_length=25)