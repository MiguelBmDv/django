from django.shortcuts import render,redirect,HttpResponse
from miapp.models import Article
from django.db import connection



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


def crear_articulo(request, title, content, public):

    #PLANTILLA: crear-articulo/Poro/Adorable peluche de poro/True
    articulo = Article(title= title,
                       content=content,
                       public=public,
)
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content} ")

def articulo(request):
    try:
        articulo = Article.objects.get(pk=1,public=False)
        response = f"Articulo extraido: {articulo.title} - {articulo.content} - Estado: {articulo.public} "
    except:
        response= "<strong>Articulo no encontrado </strong>"
    return HttpResponse(response)

def editar_articulo(request, id, title, content, public):
    articulo = Article.objects.get(pk=id)
    articulo.id=2
    articulo.title= title
    articulo.content= content
    articulo.public=public   
    articulo.save()
    return HttpResponse(f"El articulo {articulo.id} de nombre {articulo.title} ha sido actualizado y su estado es: {articulo.public}")

def articulos(request):
    # ordenar por algun campo
    articulos = Article.objects.order_by('id')
    #filtrar por campo
    articulos= Article.objects.filter(title= "Katarina")
    #filtrar por campo + and
    articulos= Article.objects.filter(title= "Katarina",public=True)
    #filtrar con lookups
    articulos= Article.objects.filter(title__contains="umi")
    articulos= Article.objects.filter(title__exact="umi")
    articulos= Article.objects.filter(title__iexact="yuumi")
    articulos= Article.objects.filter(id__gt=2)
    articulos= Article.objects.filter(id__in=[2,15])
    articulos= Article.objects.filter(title__contains="Kat").exclude(public=True)
    # articulos= Article.objects.raw("SELECT * FROM miapp_Article where content like 'l%' AND public = 1")
    articulos = Article.objects.order_by('id')

    return render (request,'articulos.html',{
        'articulos':articulos
    })

def eliminar_articulo(request, id):
    articulo= Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulosLista')   


#editar-articuloSQL/20/testeado/Aqui se hizo un cambio/False

def editar_articulo_sql(request, id, title, content, public):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE miapp_Article SET title=%s, content=%s, public=%s WHERE id=%s", [title, content, public, id])
    return redirect('articulosLista')

def eliminar_articulo_sql(request, id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM miapp_article WHERE id=%s", [id])
    return redirect('articulosLista')
