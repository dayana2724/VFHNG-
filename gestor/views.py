from django.shortcuts import render

# Create your views here.

def inicio(request):
    contexto={}
    return render(request,"inicio.html", contexto)


def list_productos(request):
    producto=['portatil lenovo', 'iphone galaxias','rolex titan']
    contexto={'listado':producto}
    return render(request,"list_productos.htm", contexto)