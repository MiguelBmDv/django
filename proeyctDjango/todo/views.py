from django.shortcuts import render
from .models import Tarea

def home(request):
    tareas= Tarea.objects.all()
    context={'tareas':tareas}
    return render(request, 'todo/home.html', context)
# Create your views here.
