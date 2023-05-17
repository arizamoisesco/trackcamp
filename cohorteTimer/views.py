from django.shortcuts import render
from .models import Teacher, Program, Cohorte
from .forms import RegisterForm

def record_time(request):

    form = RegisterForm()     
    return render(request, 'register.html', {'form': form})
