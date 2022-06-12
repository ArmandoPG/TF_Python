from django.contrib import admin

# Register your models here.
from gestionMenu.models import *


class IngredientesAdmin(admin.ModelAdmin):
    list_display = ["nombre", "tipo"]
    search_fields = ["nombre"]


class Tipo_IngredienteAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]


class PlatillosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion", "precio", "tipo"]
    search_fields = ["nombre"]


class UsuariosAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellidos", "nom_usuario", "contrasena", "tipo"]
    search_fields = ["nombre"]


class Tipo_UsuarioAdmin(admin.ModelAdmin):
    list_display = ["tipo"]
    search_fields = ["tipo"]


class Tipo_ComidaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]


class MesasAdmin(admin.ModelAdmin):
    list_display = ["nSerie"]
    search_fields = ["nSerie"]


class BebidasAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "tipo"]
    search_fields = ["nombre"]


class Tipo_BebidaAdmin(admin.ModelAdmin):
    list_display = ["categoria"]
    search_fields = ["categoria"]


admin.site.register(Ingredientes, IngredientesAdmin)
admin.site.register(Tipo_Ingrediente, Tipo_IngredienteAdmin)
admin.site.register(Platillos, PlatillosAdmin)
admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Tipo_Usuario, Tipo_UsuarioAdmin)
admin.site.register(Tipo_Comida, Tipo_ComidaAdmin)
admin.site.register(Mesas, MesasAdmin)
admin.site.register(Bebidas, BebidasAdmin)
admin.site.register(Tipo_Bebida, Tipo_BebidaAdmin)