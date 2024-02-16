from django.shortcuts import render,redirect,HttpResponse

def inicio(request):
    return render(request,'index.html')

def hola_Mundo(request):
    return render(request,'hola_mundo.html')

def saludo(request):
    return render(request,'saludo.html')

def presentacion(request):
    return render(request,'presentacion.html')

def quienesSomos(request):
    return render(request, 'acercaDe.html')

def pys(request):
    return render (request, 'pys.html')

def clase (request ):
    template = """
                    <h1>Inicio</h1>
                    <p>Años desde el 2024 hasta 2050</p>
                    <ul>
                """
    year=2024
    while year <= 2050:
        template += f"<li> {str(year)} </li>"
        year += 1
    template += """</ul><hr>"""


    template += """
                    <h1>Años biciestos</h1>
                    <ul>
                """
    year1 = 2024
    while year1 <= 2050:
        if year1 % 4 == 0:
            template += f"<li>{str(year1)}</li>"
        year1 += 1
    template += """</ul><hr>"""

    template += """
                <h1>Años pares</h1>
                <ul>
                """
    year2 = 2024
    while year2 <= 2050:
        if year2 % 2 == 0:
            template += f"<li>{str(year2)}</li>"
        year2 += 1
    template += """</ul><hr>"""
    return render(request,'years.html')


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
    return render(request,'contacto.html')

