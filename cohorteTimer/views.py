from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm
from django.views.decorators.http import require_POST

from datetime import datetime, timedelta

def record_time(request):
    if request.method == "POST":
        form = RegisterForm(data = request.POST)
        
        if form.is_valid():
            start_date = form.cleaned_data['start_cohorte']
            cohorte_duration = form.cleaned_data['duration_cohorte']
            end_time = time_cohorte(start_date, cohorte_duration)
            print(end_time)
            #return HttpResponseRedirect('result')
            return render(request, "register.html", {'end_time':end_time})
    else:
        form = RegisterForm()     
    return render(request, 'register.html', {'form': form})

# función para el calculo de cohorte
# Inputs: Fecha inicio, duracion_cohorte 
def time_cohorte(start_date, cohorte_duration):
    #Comprobamos que la información ingresada por el usuario tenga la fecha correcta
    #date = datetime.strptime(start_date, "%d/%m/%Y")
    # Convertimos los meses ingresados en dias
    month_days = 20
    month_days_totales = cohorte_duration * month_days
    # Sumamos los valores para hacer el calculo
    future_date = start_date + timedelta(days=month_days_totales)
    return future_date

# Función para mostrar el resultado en un template
@require_POST
def result(response):
    form = RegisterForm()
    # print(form)
    return render(response, 'result.html', {"form": form})