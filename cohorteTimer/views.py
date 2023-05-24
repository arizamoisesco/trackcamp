from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm

from datetime import datetime

def record_time(request):
    if request.method == "POST":
        form = RegisterForm(data = request.POST)
        
        if form.is_valid():
            dato = form.cleaned_data['name_cohorte']
            return HttpResponseRedirect('result')
    else:
        form = RegisterForm()     
    return render(request, 'register.html', {'form': form})

# función para el calculo de cohorte
# Inputs: Fecha inicio, duracion_cohorte 
def time_cohorte(start_date, cohorte_duration):
    #Comprobamos que la información ingresada por el usuario tenga la fecha correcta
    date = datetime.strptime(start_date, "%d/%m/%Y")
    # Convertimos los meses ingresados en dias
    # Sumamos los valores para hacer el calculo

# Función para mostrar el resultado en un template
def result(response):
    form = RegisterForm()
    # print(form)
    return render(response, 'result.html', {"form": form})