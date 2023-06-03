from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm
from django.views.decorators.http import require_POST

from datetime import datetime, timedelta, date
import holidays

def record_time(request):
    if request.method == "POST":
        form = RegisterForm(data = request.POST)
        
        if form.is_valid():
            start_date = form.cleaned_data['start_cohorte']
            cohorte_duration = form.cleaned_data['duration_cohorte']
            end_time = time_cohorte(start_date, cohorte_duration)
            festives_days = get_colombian_festivities(start_date,end_time)
            print(f" Contidad de dias festivos: {festives_days}")
            print(end_time)
            end_time += timedelta(days=festives_days)
            #return HttpResponseRedirect('result')
            return render(request, "register.html", {'cohorte_duration': cohorte_duration, 'start_date': start_date, 'end_time':end_time, 'festives_days': festives_days})
    else:
        form = RegisterForm()     
    return render(request, 'register.html', {'form': form})

# función para el calculo de cohorte
# Inputs: Fecha inicio, duracion_cohorte 
def time_cohorte(start_date, cohorte_duration):
    #Comprobamos que la información ingresada por el usuario tenga la fecha correcta
    #date = datetime.strptime(start_date, "%d/%m/%Y")
    # Convertimos los meses ingresados en dias
    #Cantidad de dias estandar en un mes (se tienen en cuenta todos para poder dar avance con el tema)
    month_days = 30
    month_days_totales = cohorte_duration * month_days
    print(month_days_totales)
    # Sumamos los valores para hacer el calculo
    future_date = start_date + timedelta(days=month_days_totales)
    return future_date

#Crear la función que determine los días festivos en Colombia
def get_colombian_festivities(start_date, end_date):
    festivals = holidays.CO(years=2023)
    #festivals_list = date(2023, 1, 1) in festivals
    #count_festivals = len(festivals)
    date_festivals = festivals.keys()
    #festivals_list = [feast for feast in festivals if feast["date"].isocalendar()[0] == year][::-1]
    segment_date = [fecha for fecha in date_festivals if start_date <= fecha <= end_date]
    count_segment_date = len(segment_date)
    return count_segment_date
    

# Función para mostrar el resultado en un template
@require_POST
def result(response):
    form = RegisterForm()
    # print(form)
    return render(response, 'result.html', {"form": form})