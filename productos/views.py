from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse 
from .models import Producto
from .forms import ProductoForm

#metodo que devuelva el json 
def Lista_productos(request):
    #obtener todas las instancias de la tabla
    productos = Producto.objects.all()
    #Construir una variable en formato de diccionario
    #porque el jsonResponse necesita un diccionario
    data = [
        {
            'nombre':producto.nombre,
            'precio':producto.precio,
            'imagen':producto.imagen
        }
        for producto in productos
    ]
    #devolver la respuesta en formato json
    return JsonResponse(data, safe=False)

def indexProductos(request):
    return render(request, 'homeProductos.html')

def registro(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro')
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})