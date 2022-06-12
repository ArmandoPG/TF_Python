from django.shortcuts import render
from gestionMenu.models import *
from gestionMenu.formularios import *
from django.http import HttpResponse

# Create your views here.
from gestionMenu.models import Bebidas


def error_404(request, exception):
    return render(request, "errores/404.html", {})


def principal_admin(request):
    return render(request, "administrador.html", {})


def bebidas(request):
    # BUSQUEDA
    mensaje = "No has realizado una búsqueda."
    bebida = []
    if request.method == "GET":
        busqueda = request.GET.get("txtBusqueda", "")
        if busqueda:
            mensaje = "Articulo buscado: %s" % busqueda
            bebida = Bebidas.objects.filter(nombre__icontains=busqueda)
    return render(request, "registro_bebidas.html", {"msj": mensaje, "bebida": bebida})


def agregar_bebida(request):
    # AGREGAR
    if request.method == "POST":
        bebidaFormulario = BebidasFormulario(request.POST)
        if bebidaFormulario.is_valid():
            nombre = bebidaFormulario.cleaned_data.get("nombre", "")
            precio = bebidaFormulario.cleaned_data.get("precio", "")
            tipo = bebidaFormulario.cleaned_data.get("tipo", "")
            a = Bebidas(nombre=nombre, precio=precio, tipo=Tipo_Bebida.objects.get(id=tipo))
            a.save()
            return HttpResponse("Gracias, se ha guardado el nuevo artículo.")
    else:
        bebidaFormulario = BebidasFormulario()
    return render(request, "agregar_bebida.html", {"form": bebidaFormulario})


def modificar_bebidas(request, id):
    # MODIFICAR
    id_bebida = Bebidas.objects.get(id=id)
    if request.method == "POST":
        bebidaFormulario = BebidasFormulario(request.POST)
        if bebidaFormulario.is_valid():
            nombre = bebidaFormulario.cleaned_data.get("nombre", "")
            precio = bebidaFormulario.cleaned_data.get("precio", "")
            tipo = bebidaFormulario.cleaned_data.get("tipo", "")

            id_bebida.nombre = nombre
            id_bebida.precio = precio
            id_bebida.tipo = Tipo_Bebida.objects.get(id=tipo)
            id_bebida.save()
        return HttpResponse("Gracias, se ha editado el artículo.")
    else:
        dict_bebida = {"nombre": id_bebida.nombre,
                       "precio": id_bebida.precio,
                       "tipo": id_bebida.tipo.id
                       }
        bebidaFormulario = BebidasFormulario(dict_bebida)
    return render(request, "modificar_bebidas.html", {"form": bebidaFormulario})


def ingredientes(request):
    # BUSQUEDA
    mensaje = "No has realizado una búsqueda."
    ingrediente = []
    if request.method == "GET":
        busqueda = request.GET.get("txtBusqueda", "")
        if busqueda:
            mensaje = "Articulo buscado: %s" % busqueda
            ingrediente = Ingredientes.objects.filter(nombre__icontains=busqueda)
    return render(request, "registro_ingredientes.html", {"msj": mensaje, "ingrediente": ingrediente})


def agregar_ingrediente(request):
    # AGREGAR
    if request.method == "POST":
        ingredienteFormulario = IngredientesFormulario(request.POST)
        if ingredienteFormulario.is_valid():
            nombre = ingredienteFormulario.cleaned_data.get("nombre", "")
            tipo = ingredienteFormulario.cleaned_data.get("tipo", "")
            a = Ingredientes(nombre=nombre, tipo=Tipo_Ingrediente.objects.get(id=tipo))
            a.save()
            return HttpResponse("Gracias, se ha guardado el nuevo artículo.")
    else:
        ingredienteFormulario = IngredientesFormulario()
    return render(request, "agregar_ingrediente.html", {"form": ingredienteFormulario})


def modificar_ingrediente(request, id):
    # MODIFICAR
    id_ingrediente = Ingredientes.objects.get(id=id)
    if request.method == "POST":
        ingredienteFormulario = IngredientesFormulario(request.POST)
        if ingredienteFormulario.is_valid():
            nombre = ingredienteFormulario.cleaned_data.get("nombre", "")
            tipo = ingredienteFormulario.cleaned_data.get("tipo", "")

            id_ingrediente.nombre = nombre
            id_ingrediente.tipo = Tipo_Ingrediente.objects.get(id=tipo)
            id_ingrediente.save()
        return HttpResponse("Gracias, se ha editado el artículo.")
    else:
        dict_ingrediente = {"nombre": id_ingrediente.nombre,
                            "tipo": id_ingrediente.tipo.id
                            }
        ingredienteFormulario = IngredientesFormulario(dict_ingrediente)
    return render(request, "modificar_ingrediente.html", {"form": ingredienteFormulario})


def mesas(request):
    # BUSQUEDA
    mensaje = "No has realizado una búsqueda."
    mesa = []
    if request.method == "GET":
        busqueda = request.GET.get("txtBusqueda", "")
        if busqueda:
            mensaje = "Articulo buscado: %s" % busqueda
            mesa = Mesas.objects.filter(nSerie=busqueda)
    # return render(request, "registro_ingredientes.html", {"msj": mensaje, "ingrediente": ingrediente})
    return render(request, "registro_mesas.html", {"msj": mensaje, "mesa": mesa})


def agregar_mesa(request):
    # AGREGAR
    if request.method == "POST":
        mesaFormulario = MesasFormulario(request.POST)
        if mesaFormulario.is_valid():
            nSerie = mesaFormulario.cleaned_data.get("nSerie", "")
            a = Mesas(nSerie=nSerie)
            a.save()
            return HttpResponse("Gracias, se ha guardado la mesa.")
    else:
        mesaFormulario = MesasFormulario()
    return render(request, "agregar_mesa.html", {"form": mesaFormulario})


def modificar_mesa(request, nSerie):
    # MODIFICAR
    id_mesa = Mesas.objects.get(nSerie=nSerie)
    if request.method == "POST":
        mesaFormulario = MesasFormulario(request.POST)
        if mesaFormulario.is_valid():
            nSerie = mesaFormulario.cleaned_data.get("nSerie", "")

            id_mesa.nSerie = nSerie
            id_mesa.save()
        return HttpResponse("Gracias, se ha editado la mesa.")
    else:
        dict_mesa = {"nSerie": id_mesa.nSerie
                     }
        mesaFormulario = MesasFormulario(dict_mesa)
    return render(request, "modificar_mesa.html", {"form": mesaFormulario})


def platillos(request):
    # BUSQUEDA
    mensaje = "No has realizado una búsqueda."
    platillo = []
    if request.method == "GET":
        busqueda = request.GET.get("txtBusqueda", "")
        if busqueda:
            mensaje = "Articulo buscado: %s" % busqueda
            platillo = Platillos.objects.filter(nombre__icontains=busqueda)
    return render(request, "registro_platillos.html", {"msj": mensaje, "platillo": platillo})


def agregar_platillo(request):
    # AGREGAR
    if request.method == "POST":
        platilloFormulario = PlatillosFormulario(request.POST)
        if platilloFormulario.is_valid():
            nombre = platilloFormulario.cleaned_data.get("nombre", "")
            descripcion = platilloFormulario.cleaned_data.get("descripcion", "")
            tipo = platilloFormulario.cleaned_data.get("tipo", "")
            precio = platilloFormulario.cleaned_data.get("precio", "")
            a = Platillos(nombre=nombre, descripcion=descripcion, precio=precio, tipo=Tipo_Comida.objects.get(id=tipo))
            a.save()
            return HttpResponse("Gracias, se ha guardado el nuevo platillo.")
    else:
        platilloFormulario = PlatillosFormulario()
    return render(request, "agregar_platillo.html", {"form": platilloFormulario})


def modificar_platillo(request, id):
    # MODIFICAR
    id_platillo = Platillos.objects.get(id=id)
    if request.method == "POST":
        platilloFormulario = PlatillosFormulario(request.POST)
        if platilloFormulario.is_valid():
            nombre = platilloFormulario.cleaned_data.get("nombre", "")
            descripcion = platilloFormulario.cleaned_data.get("descripcion", "")
            precio = platilloFormulario.cleaned_data.get("precio", "")
            tipo = platilloFormulario.cleaned_data.get("tipo", "")

            id_platillo.nombre = nombre
            id_platillo.descripcion = descripcion
            id_platillo.precio = precio
            id_platillo.tipo = Tipo_Comida.objects.get(id=tipo)
            id_platillo.save()
        return HttpResponse("Gracias, se ha editado el platillo.")
    else:
        dict_platillo = {"nombre": id_platillo.nombre,
                         "descripcion": id_platillo.descripcion,
                         "precio": id_platillo.precio,
                         "tipo": id_platillo.tipo.id
                         }
        platilloFormulario = PlatillosFormulario(dict_platillo)
    return render(request, "modificar_platillo.html", {"form": platilloFormulario})


def usuarios(request):
    # BUSQUEDA
    mensaje = "No has realizado una búsqueda."
    usuario = []
    if request.method == "GET":
        busqueda = request.GET.get("txtBusqueda", "")
        if busqueda:
            mensaje = "Articulo buscado: %s" % busqueda
            usuario = Usuarios.objects.filter(nombre__icontains=busqueda)
    return render(request, "registro_usuarios.html", {"msj": mensaje, "usuario": usuario})


def agregar_usuario(request):
    # AGREGAR
    if request.method == "POST":
        usuarioFormulario = UsuariosFormulario(request.POST)
        if usuarioFormulario.is_valid():
            nombre = usuarioFormulario.cleaned_data.get("nombre", "")
            apellidos = usuarioFormulario.cleaned_data.get("apellidos", "")
            nom_usuario = usuarioFormulario.cleaned_data.get("nom_usuario", "")
            contrasena = usuarioFormulario.cleaned_data.get("contrasena", "")
            tipo = usuarioFormulario.cleaned_data.get("tipo", "")
            a = Usuarios(nombre=nombre, apellidos=apellidos, nom_usuario=nom_usuario, contrasena=contrasena,
                         tipo=Tipo_Usuario.objects.get(id=tipo))
            a.save()
            return HttpResponse("Gracias, se ha guardado el nuevo usuario.")
    else:
        usuarioFormulario = UsuariosFormulario()
    return render(request, "agregar_usuario.html", {"form": usuarioFormulario})


def modificar_usuario(request, id):
    # MODIFICAR
    id_usuario = Usuarios.objects.get(id=id)
    if request.method == "POST":
        usuarioFormulario = UsuariosFormulario(request.POST)
        if usuarioFormulario.is_valid():
            nombre = usuarioFormulario.cleaned_data.get("nombre", "")
            apellidos = usuarioFormulario.cleaned_data.get("apellidos", "")
            nom_usuario = usuarioFormulario.cleaned_data.get("nom_usuario", "")
            contrasena = usuarioFormulario.cleaned_data.get("contrasena", "")
            tipo = usuarioFormulario.cleaned_data.get("tipo", "")

            id_usuario.nombre = nombre
            id_usuario.apellidos = apellidos
            id_usuario.nom_usuario = nom_usuario
            id_usuario.contrasena = contrasena
            id_usuario.tipo = Tipo_Usuario.objects.get(id=tipo)
            id_usuario.save()
        return HttpResponse("Gracias, se ha editado el usuario.")
    else:
        dict_usuario = {"nombre": id_usuario.nombre,
                        "apellidos": id_usuario.apellidos,
                        "nom_usuario": id_usuario.nom_usuario,
                        "contrasena": id_usuario.contrasena,
                        "tipo": id_usuario.tipo.id
                        }
        usuarioFormulario = UsuariosFormulario(dict_usuario)
    return render(request, "modificar_usuario.html", {"form": usuarioFormulario})
