"""Menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionMenu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("principal_admin", views.principal_admin, name="principal_admin"),
    path("bebidas", views.bebidas, name="bebidas"),
    path("agregar_bebida", views.agregar_bebida, name="agregar_bebida"),
    path("modificar_bebidas/<int:id>", views.modificar_bebidas, name="modificar_bebidas"),
    path("ingredientes", views.ingredientes, name="ingredientes"),
    path("agregar_ingrediente", views.agregar_ingrediente, name="agregar_ingrediente"),
    path("modificar_ingrediente/<int:id>", views.modificar_ingrediente, name="modificar_ingrediente"),
    path("mesas", views.mesas, name="mesas"),
    path("modificar_mesa/<int:nSerie>", views.modificar_mesa, name="modificar_mesa"),
    path("agregar_mesa", views.agregar_mesa, name="agregar_mesa"),
    path("platillos", views.platillos, name="platillos"),
    path("agregar_platillo", views.agregar_platillo, name="agregar_platillo"),
    path("modificar_platillo/<int:id>", views.modificar_platillo, name="modificar_platillo"),
    path("usuarios", views.usuarios, name="usuarios"),
    path("agregar_usuario", views.agregar_usuario, name="agregar_usuario"),
    path("modificar_usuario/<int:id>", views.modificar_usuario, name="modificar_usuario"),
]


handler404 = "gestionMenu.views.error_404"
