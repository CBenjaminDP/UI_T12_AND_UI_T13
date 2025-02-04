from django.http import HttpResponse
from django.shortcuts import render
from app.utils import google_search
from django.http import JsonResponse
from .models import Usuarios
def index(request):
    return HttpResponse('<br>Hola Mundo</br>')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

def error(request, exception):
    return 7/0

def onepage(request):
    return render(request, 'onepage.html', status=200)

def prueba(request):
    #como obtener información de un html
    nombre = request.GET.get('nombre','')
    edad = request.GET.get('edad','')
    persona= {'nombre':nombre, 'edad':edad, 'descripcion':nombre + ' tiene ' + edad + ' años'}
    persona1= {'nombre':'Benjamin', 'edad':20, 'descripcion':nombre + ' tiene ' + edad + ' años'}
    persona2= {'nombre':'Jassiel', 'edad':21, 'descripcion':nombre + ' tiene ' + edad + ' años'}
    if(persona['nombre'] == 'Jesus'):
        persona['descripcion'] = 'Binevenido Usuario Jesus'
    print(persona['nombre'])
    conjunto = [persona,persona1,persona2]	
    return render(
        request, 
        'prueba.html',
        {'objeto':persona, 'mensaje':'Hola Mundo', 'personas':conjunto})

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "practica.html", {"results": results, "query": query})


def error_logs(request):
    return render(request, 'dataTables.html')

def get_error_logs(request):
    errors = Usuarios.objects.values('id', 'nombre', 'apellidos', 'matricula', 'edad')
    return JsonResponse({'data': list(errors)})