# views.py
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Categoria
from .forms import CategoriaForm

def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_categoria')  # Redirige a la misma página después de registrar
    else:
        form = CategoriaForm()

    # Obtener todas las categorías para mostrarlas en el mismo HTML
    categorias = Categoria.objects.all()
    return render(request, 'registrar_categoria.html', {'form': form, 'categorias': categorias})


# Vista para obtener todas las categorías en formato JSON
def get_categorias(request):
    categorias = list(Categoria.objects.values())
    return JsonResponse({'categorias': categorias})

# Vista para mostrar las categorías en tarjetas
def mostrar_categorias(request):
    return render(request, 'categorias.html')