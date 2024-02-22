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
    template = """Inicio """
    
    year=2024
    while year <= 2050:
        template += f" {str(year)}"
        year += 1
    # template += """</ul><hr>"""
    

    # template += """Años biciestos"""
    
    year1 = 2024
    while year1 <= 2050:
        if year1 % 4 == 0:
            template += f"{str(year1)}"            
            # template += f"<li>{str(year1)}</li>"
        year1 += 1
    # template += """</ul><hr>"""

    # template += """Años pares"""
    
    year2 = 2024
    while year2 <= 2050:
        if year2 % 2 == 0:
            template += f"{str(year2)}"            
            # template += f"<li>{str(year2)}</li>"
        year2 += 1
    # template += """</ul><hr>"""
    return render(request,'years.html',{
        'miVariable':'Hola, soy un gato que ta en la vista',
        'title':'Años 2024-2050',
        'titlePag':'Listado de años',
        'template':template,
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
        
    
    contact= """
            Bienvenido al apartado de contactos :
            """
    return render(request,'contacto.html')

