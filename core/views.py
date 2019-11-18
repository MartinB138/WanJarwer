from django.shortcuts import render, redirect
from django.views import generic
from .models import Proce, Graph, Ram, Gab, Marca_Proce, Marca_Graph, Marca_Gab
from django.contrib import messages
from django.views.generic.edit import CreateView


# Create your views here.

def home(request):
    return render(request, 'core/home.html')
def proc(request):

    #CRUD listado
    proc = Proce.objects.all()
    marca = Marca_Proce.objects.all()

    #CRUD AGREGAR
    variables = {
        'proc':proc,
        'marca':marca 
    }
    if request.POST:
        proc = Proce()
        marca = Marca_Proce()
        marca.id = request.POST.get('cbMarca')
        proc.proce = marca
        proc.proceN = request.POST.get('txtNombre')
        proc.core = request.POST.get('txtCore')
        proc.threads = request.POST.get('txtHilos')
        proc.frecMini = request.POST.get('txtFrecMi')
        proc.frecMax = request.POST.get('txtFrecMa')

        try:
            proc.save()
            variables['mensaje'] = 'Guardado correctamente'
        except: 
            variables['mensaje'] = 'No se ha podido guardar'
            
    
    
    
    return render(request, 'core/proc.html', variables)

def graf(request):
    #CRUD listado
    graf = Graph.objects.all()
    marcag = Marca_Graph.objects.all()

    #CRUD AGREGAR
    variables = {
        'graf':graf,
        'marcag':marcag
    }
    if request.POST:
        graf = Graph()
        marcag = Marca_Graph()
        marcag.id = request.POST.get('cbMarca')
        graf.graph = marcag
        graf.graphN = request.POST.get('txtNombre')
        graf.gb = request.POST.get('txtGb')
        graf.frecMin = request.POST.get('txtFrec')

        try:
            graf.save()
            variables['mensaje'] = 'Guardado correctamente'
        except: 
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/graf.html', variables)


def ram(request):
    #CRUD listado
    ram = Ram.objects.all()

    #CRUD AGREGAR
    variables = {
        'ram':ram
    }
    if request.POST:
        ram = Ram()
        ram.marcr = request.POST.get('txtMarca')
        ram.nomr = request.POST.get('txtNombre')
        ram.gbs = request.POST.get('txtGb')
        ram.frecMinn = request.POST.get('txtFrec')
        ram.volt = request.POST.get('txtVolt')

        try:
            ram.save()
            variables['mensaje'] = 'Guardado correctamente'
        except: 
            variables['mensaje'] = 'No se ha podido guardar'
    return render(request, 'core/ram.html', variables)
def gab(request):
    #CRUD listado
    gab = Gab.objects.all()
    marcaga = Marca_Gab.objects.all()

    #CRUD AGREGAR
    variables = {
        'gab':gab,
        'marcaga':marcaga
    }
    if request.POST:
        gab = Gab()
        marcaga = Marca_Gab()
        marcaga.id = request.POST.get('cbTipo')
        gab.tipo_gabinete = marcaga
        gab.marca_gabinete = request.POST.get('txtMarca')
        gab.nombre_gabinete = request.POST.get('txtNombre')
        
        
        try:
            gab.save()
            variables['mensaje'] = 'Guardado correctamente'
        except: 
            variables['mensaje'] = 'No se ha podido guardar'
    return render(request, 'core/gab.html', variables)
def log(request):
    return render(request, 'core/login.html')
def sig(request):
    return render(request, 'core/register.html')

#CRUD eliminar proce

def eliminar_proce(request, id):

    proc = Proce.objects.get(id=id)
    try:
        proc.delete()
        mensaje = '(Eliminado correctamente)'
        messages.success(request, mensaje)
    except:
        mensaje = '(No se a podido eliminar)'
        messages.error(request, mensaje)

    return redirect ('proc')

#CRUD eliminar graf
def eliminar_graf(request, id):

    graf = Graph.objects.get(id=id)
    try:
        graf.delete()
        mensaje = '(Eliminado correctamente)'
        messages.success(request, mensaje)
    except:
        mensaje = '(No se a podido eliminar)'
        messages.error(request, mensaje)

    return redirect ('graf')

#CRUD eliminar ram
def eliminar_ram(request, id):

    ram = Ram.objects.get(id=id)
    try:
        ram.delete()
        mensaje = '(Eliminado correctamente)'
        messages.success(request, mensaje)
    except:
        mensaje = '(No se a podido eliminar)'
        messages.error(request, mensaje)

    return redirect ('ram')

#CRUD eliminar Gabinete
def eliminar_gab(request, id):

    gab = Gab.objects.get(id=id)
    try:
        gab.delete()
        mensaje = '(Eliminado correctamente)'
        messages.success(request, mensaje)
    except:
        mensaje = '(No se a podido eliminar)'
        messages.error(request, mensaje)

    return redirect ('gab')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#CRUD modificar proce
def modificar_proce(request, id):
    #buscar procesador para que se pueda modificar
    proce = Proce.objects.get(id=id)
    marca = Marca_Proce.objects.all()

    variables = {
        'proce':proce,
        'marca':marca
    }

    if request.POST:
        proce = Proce()
        proce.id = request.POST.get('txtId')
        marca = Marca_Proce()
        marca.id = request.POST.get('cbMarca')
        proce.proce = marca
        proce.proceN = request.POST.get('txtNombre')
        proce.core = request.POST.get('txtCore')
        proce.threads = request.POST.get('txtHilos')
        proce.frecMini = request.POST.get('txtFrecMi')
        proce.frecMax = request.POST.get('txtFrecMa')
        
        try:
            proce.save()
            messages.success(request, '(Modificado Correctamente)')
        except: 
            messages.error(request, '(No se ha podido modificar)')
        return redirect('proc')


    return render(request, 'core/modificar_proce.html', variables)

#CRUD modificar graf

def modificar_graf(request, id):
    #buscar procesador para que se pueda modificar
    graf = Graph.objects.get(id=id)
    marcag = Marca_Graph.objects.all()

    variables = {
        'graf':graf,
        'marcag':marcag
    }

    if request.POST:
        graf = Graph()
        marcag = Marca_Graph()
        marcag.id = request.POST.get('cbMarca')
        graf.graph = marcag
        graf.id = request.POST.get('txtId')
        graf.graphN = request.POST.get('txtNombre')
        graf.gb = request.POST.get('txtGb')
        graf.frecMin = request.POST.get('txtFrec')
        

        try:
            graf.save()
            messages.success(request, '(Modificado Correctamente)')
        except: 
            messages.error(request, '(No se ha podido modificar)')
        return redirect('graf')


    return render(request, 'core/modificar_graf.html', variables)

    #CRUD modificar ram

def modificar_ram(request, id):
    #buscar procesador para que se pueda modificar
    ram = Ram.objects.get(id=id)
    
    variables = {
        'ram':ram
    }

    if request.POST:
        ram = Ram()
        ram.id = request.POST.get('txtId')
        ram.marcr = request.POST.get('txtMarca')
        ram.nomr = request.POST.get('txtNombre')
        ram.gbs = request.POST.get('txtGb')
        ram.frecMinn = request.POST.get('txtFrec')
        ram.volt = request.POST.get('txtVolt')
        

        try:
            ram.save()
            messages.success(request, '(Modificado Correctamente)')
        except: 
            messages.error(request, '(No se ha podido modificar)')
        return redirect('ram')


    return render(request, 'core/modificar_ram.html', variables)

def modificar_gab(request, id):
    #buscar procesador para que se pueda modificar
    gab = Gab.objects.get(id=id)
    marcaga = Marca_Gab.objects.all()
    
    variables = {
        'gab':gab,
        'marcaga':marcaga
    }

    if request.POST:
        gab = Gab()
        marcaga = Marca_Gab()
        marcaga.id = request.POST.get('cbTipo')
        gab.tipo_gabinete = marcaga
        
        gab.id = request.POST.get('txtId')
        gab.marca_gabinete = request.POST.get('txtMarca')
        gab.nombre_gabinete = request.POST.get('txtNombre')
        
        
        
        try:
            gab.save()
            messages.success(request, '(Modificado Correctamente)')
        except: 
            messages.error(request, '(No se ha podido modificar)')
        return redirect('gab')


    return render(request, 'core/modificar_gab.html', variables)
    
def filtro_proce(request):
    proce = Proce.objects.all()
    
    variables = {
        'proce':proce
         
    }
    if request.POST.get('nommarc'):
        nommarc=request.POST.get('nommarc')
        proce=proce.filter(proce__contains=nommarc)

    return render(request, 'core/filtro_proce.html', variables)
    
