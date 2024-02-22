from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path ('inicio/', views.inicio,name="inicio"),
    path ("years/",views.clase,name="clase"),
    path ("contacto/",views.contacto,name="contacto"),
    path ("contacto/<str:name>",views.contacto,name="contacto"),
    path ("contacto/<str:name>/<str:lastname>",views.contacto,name="contacto"),
    path('hola_mundo/', views.hola_Mundo,name="hola_mundo"),
    path('saludo/', views.saludo,name="saludo"),
    path('presentacion/', views.presentacion,name="presentacion"),
    path('pys/', views.pys,name="pys"),
    path('acercaDe/', views.quienesSomos, name="acercaDe"),
]