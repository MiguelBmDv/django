from django.shortcuts import render,redirect,HttpResponse

def inicio(request):
    return render(request,'index.html')

def hola_Mundo(request):
    lista = []
    i = 0
    while i < 5:
        lista.append("Mundo dice hola")
        i += 1
    return render(request,'hola_mundo.html', {
        'lista': lista
        })

def saludo(request):
    lista_saludos = ["¡Hola!", "¡Buenos días!", "¡Buenas tardes!", "¡Buenas noches!", "¡Hola de nuevo!"]

    return render(request,'saludo.html', {
        'lista_saludos': lista_saludos
        })

def presentacion(request):
    lista_aspectos = []
    i = 0
    while i < 5:
        lista_aspectos.append(f"Aspecto {i+1}")
        i += 1

    return render(request,'presentacion.html',{
        'lista_aspectos': lista_aspectos
        })

def quienesSomos(request):
    return render(request, 'acercaDe.html')

def pys(request):
    return render (request, 'pys.html')

def clase (request ):
    name="Miguel Angel Bernal"
    años = [año for año in range(2024, 2051)]
    añosPares = [año for año in años if año % 2 == 0]
    añosImpares = [año for año in años if año % 2 != 0]
    añosBisiestos = [año for año in años if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)]

    return render(request,'years.html',{
        'name':name,
        'title':'Años 2024-2050',
        'titlePag':'Listado de años',
        'años': años,
        'años_pares': añosPares,
        'años_impares': añosImpares, 
        'años_bisiestos': añosBisiestos,
    })



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

    letras=['A','B','C','D']
    
    return render(request,'contacto.html', {
        'texto':'Creanmen',
        'letra':letras
    })

