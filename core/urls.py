from django.urls import path
from .views import home,proc,graf,ram,gab,log,sig,eliminar_proce,modificar_proce, eliminar_graf, modificar_graf,eliminar_ram,modificar_ram,eliminar_gab,modificar_gab, filtro_proce
from . import views

urlpatterns = [
    path('', home, name = "home"),
    path('proc', proc, name = "proc"),
    path('graf', graf, name = "graf"),
    path('ram', ram, name = "ram"),
    path('gab', gab, name = "gab"),
    path('log', log, name = "log"),
    path('sig', sig, name = "sig"),
    path('eliminar_proce/<id>/', eliminar_proce, name="eliminar_proce"),
    path('modificar_proce/<id>/', modificar_proce, name="modificar_proce"),
    path('eliminar_graf/<id>/', eliminar_graf, name="eliminar_graf"),
    path('modificar_graf/<id>/', modificar_graf, name="modificar_graf"),
    path('eliminar_ram/<id>/', eliminar_ram, name="eliminar_ram"),
    path('modificar_ram/<id>/', modificar_ram, name="modificar_ram"),
    path('eliminar_gab/<id>/', eliminar_gab, name="eliminar_gab"),
    path('modificar_gab/<id>/', modificar_gab, name="modificar_gab"), 
    path('filtro_proce', filtro_proce, name = "filtro_proce")
]

