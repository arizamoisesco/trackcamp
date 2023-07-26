from django.shortcuts import render
from .forms import RegisterForm

def months_calculation (request):
    hour_month_aprox = 30 * 24

    if request.method == "POST":
        form = RegisterForm(data = request.POST)

        if form.is_valid():

            #Valores de los campos del formulario
            
            total_hours_course = form.cleaned_data['hours_total_number']

            hourly_intensity = form.cleaned_data['hourly_intensity']

            #Realizamos sus respectivas operaciones
            total_hours_delay = total_hours_course / hourly_intensity
            print(total_hours_delay)

            month_delay_aprox = round(total_hours_delay / hour_month_aprox)
            print(month_delay_aprox)

            return render(request, 'month_calculate.html')

    else: 
        form = RegisterForm()
    
    return render(request, 'month_calculate.html', {'form': form})
