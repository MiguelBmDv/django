from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('',views.home,name="home"),
    path ("agregar/",views.agregar,name="agregar"),
    path ("eliminar/<int:tarea_id>/",views.eliminar,name="eliminar"),
    path ("editar/<int:tarea_id>/", views.editar, name="editar"),
    
    
    path ("clase/<int:redirigir>",views.clase,name="clase"),
    path ("par/",views.par,name="par"),
    path ("impar/",views.impar,name="impar"),
    path ("bisciesto/",views.bisciesto,name="bisciesto"),
    path ("contacto/",views.contacto,name="contacto"),
    path ("contacto/<str:name>",views.contacto,name="contacto"),
    path ("contacto/<str:name>/<str:lastname>",views.contacto,name="contacto"),
]
