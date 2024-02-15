from django.shortcuts import render,redirect,HttpResponse
from .models import Tarea
from .forms import TareaForm

def home(request):
    tareas= Tarea.objects.all()
    context={'tareas':tareas}
    return render(request, 'todo/home.html', context)
# Create your views here.

def agregar (request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    
    context= {'form':form}
    return render (request,'todo/agregar.html',context)

def eliminar (request,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect ("home")

def editar (request, tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance = tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=TareaForm(instance=tarea)
    context= {'form':form}
    return render (request,'todo/agregar.html',context)






layout= """
        <h1> Site Web con Miguel Bm Dev</h1>
        <hr>
        <ul>
            <li><a href="/clase">Años desde el 2024 al 2025</a></li>
            <li><a href="/par">Años pares</a></li>
            <li><a href="/impar">Años Impares</li>
            <li><a href="/bisciesto">Años bisciesto</a></li>
            <li><a href="/contacto">Contacto</a></li>
            
            <br>
            <li><a href="/">Proyecto Django!</a></li>
        </ul>      
        """
def clase (request,redirigir=0):
    if redirigir == 1:  
        return redirect('contacto',name="Miguel")
    template = """  <h1>Inicio</h1>
                    <p>Años desde el 2024 al 2050</p>
                    <ul>
                """
    year=2024
    while year <=2050:
        template += f"<li> {str(year)}   </li>"  
        year += 1
    return HttpResponse(layout+template)

def par (request): 
    template = """</ul> <hr> <br> <p> Años par </p> """
    year=2024
    while year <=2050:
        if year % 2 == 0:
            template += f" <li> {str(year)} </li>"
        year += 1
    return HttpResponse(layout+template)

def impar (request):
    template = """</ul> <hr> <br> <p> Años impares </p> """    
    year=2024
    while year <= 2050:
        if year %2 != 0:
            template += f" <li> {str(year)} </li>"
        year += 1
    return HttpResponse(layout+template)

def bisciesto (request):
    template = """</ul> <hr> <br> <p> Años bisciesto </p> """
    year=2024
    while year <= 2050:
        if year % 4 == 0:
                template += f" <li> {str(year)} </li>"
        year += 1
        
    return HttpResponse(layout+template)

def contacto (request,name="",lastname=""):
    html=""
    if name and lastname:
        html= "<h2> Nombre completo: </h2>"
        html+= f"<h2> Bienvenido {name} {lastname} </h2>"
    elif name:
        html= "<h2> Nombre sin apellido: </h2>"
        html+= f"<h2> Bienvenido {name} </h2>"
    elif lastname:
        html= "<h2> Apellido sin nombre : </h2>"
        html+= f"<h2> Bienvenido {lastname} </h2>"
    else:
        html= "<h2> Sin nombre y apellidos definidos </h2>"
        
    
    contact= """
            Bienvenido al apartado de contactos :
            """
    return HttpResponse(layout+contact+f"<h2>Contacto </2>"+html)

