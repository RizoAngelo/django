from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import persona
from .forms import DatosperForm
from django.template import Template,Context


def inicial(request):
    doc_externo = open("hoteleria/template/crud/inicio.html", encoding="utf-8")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({})
    documento = plt.render(ctx)
    return HttpResponse(documento)

def verpersona(request):
    daticos=persona.objects.all()
    return render(request, 'paginasapp/index.html', {'daticos':daticos}, encoding="utf-8")
def crearpersona(request):
    formulario = DatosperForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('verpersona')
    return render(request, 'crud/insert.html', {'formulario':formulario}, encoding="utf-8")

def editarpersona(request):
    return render(request, 'crud/editar.html', encoding="utf-8")




'''from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.shortcuts import render'''

'''
def saludo(request):#Primera vista
    return HttpResponse ("Hola Cliente Esta En Django")

def despedida(request):
    return HttpResponse ("Chao Cliente nos vemos pronto")


def plantillas(request):
    doc_externo = open("MiproyectodDjango/template/index.html", encoding="utf-8")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({})
    documento = plt.render(ctx)
    return HttpResponse(documento)


def dameFecha(request):
    fecha_actual=datetime.datetime.now()

    documento="<html><body><h1>Fecha y hora actual %s</h1></body></html>"%fecha_actual

    return HttpResponse(documento)

def calculaedad(request, fnacimiento,ffutura):
    #edadActual=18
    periodo=ffutura-fnacimiento
    edadFutura=periodo
    documento="<html><body><h1>En el Año %s Tendras %s</h1></body></html>"%(ffutura,edadFutura)

    return HttpResponse(documento)

def plantilla2(request):
    doc_externo = open("MiproyectodDjango/template/inicio_seccion.html", encoding="utf-8")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({})
    documento = plt.render(ctx)
    return HttpResponse(documento)

def registro(request):
    doc_externo = open("MiproyectodDjango/template/registro.html", encoding="utf-8")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({})
    documento = plt.render(ctx)
    return HttpResponse(documento)'''