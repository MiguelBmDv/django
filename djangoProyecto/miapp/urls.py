from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path ('inicio/', views.inicio,name="inicio"),
    path ("years/",views.clase,name="years"),
    path ("contacto/",views.contacto,name="contacto"),
    path ("contacto/<str:name>",views.contacto,name="contacto"),
    path ("contacto/<str:name>/<str:lastname>",views.contacto,name="contacto"),
    path('hola_mundo/', views.hola_Mundo,name="holaMundo"),
    path('saludo/', views.saludo,name="saludo"),
    path('presentacion/', views.presentacion,name="presentacion"),
    path('pys/', views.pys,name="pys"),
    path('acercaDe/', views.quienesSomos, name="acercaDe"),
    path('crear-articulo/',views.crear_articulo, name="createArticle"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>',views.crear_articulo, name="createArticle"),
    path('articulo/',views.articulo, name= "articulo"),
    path('editar-articulo/<int:id>/<str:title>/<str:content>/<str:public>',views.editar_articulo, name="editarArticulo"),
    path('articulos/', views.articulos, name= "articulosLista"),
]