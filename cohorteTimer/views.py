from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm

def record_time(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('result')
    else:
        form = RegisterForm()     
    return render(request, 'register.html', {'form': form})

# función para el calculo de cohorte

# Función para mostrar el resultado en un template
def result(response):
    form = RegisterForm()
    print(form)
    return render(response, 'result.html', {"form": form})