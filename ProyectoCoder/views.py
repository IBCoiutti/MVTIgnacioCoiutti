from contextvars import Context
from multiprocessing import context
from re import template
from django.http import HttpResponse



def saludo(request):
    return HttpResponse("Hola!")

def probandotemplate(self):
    mihtml = open("D:/CoderHouse/ProyectoCoder/ProyectoCoder/plantillas/template1.html")

    plantilla = template(mihtml.read())

    mihtml.close()

    micontexto = Context()

    documento = plantilla.render(micontexto)

    return HttpResponse(documento)

