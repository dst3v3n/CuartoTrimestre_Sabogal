from django.shortcuts import render
from . models import Usuario

# def usuariolist (request):
#     return render (request , 'usuarioslist.html')

def usuariolist (request):
    get_usuarios = Usuario.objects.all()
    data = {
        'get_usuarios' : get_usuarios
    }
    return render (request , 'usuarioslist.html' , data)

def metodo_post (request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        documento = request.POST['documento']
        ficha = request.POST['ficha']
        foto = request.FILES['foto']
        Usuario(nombre = nombre , documento = documento , ficha = ficha , photo = foto).save()
        return render(request , 'usuarioslist.html') 