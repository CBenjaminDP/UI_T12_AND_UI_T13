from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Usuarios
from django.shortcuts import redirect


from .utils import google_search

# Create your views here.
def index(request):
        return redirect('login')

def error_404_view(request, exception):
    render(request, '404.html', status=404)

def error_500_view(request, exception):
    render(request, '500.html', status=500)

def error(request, exception):
    return 7/0;

def onepage(request):
    return render(request, 'onepage.html', status=200)

def prueba(request):
    nombre = request.GET.get('nombre', 'No hay nombre')
    edad = request.GET.get('edad', 'No hay edad')

    persona = {
        'nombre': nombre,
        'edad': edad,
        'descripcion': nombre + ' tiene ' + edad + ' años'
    }

    if persona['nombre'] == 'Benjamin':
        persona['descripcion'] = 'Hola Benjamin'

    return render(request, 'prueba.html', {'objeto': persona, 'saludo': 'Hola mundo'})

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

def usuarios_list(request):
    return render(request, 'usuarios_list.html')

def get_usuarios(request):
    usuarios = Usuarios.objects.values('id', 'nombre', 'apellido', 'matricula', 'edad')
    return JsonResponse({'data': list(usuarios)})