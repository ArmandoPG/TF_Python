from django import forms
from gestionMenu.models import *


tipo_bebida = Tipo_Bebida.objects.all()
choices_bebida = []
for item in tipo_bebida:
    choices_bebida.append((item.id, item.categoria))
choices_bebida = tuple(choices_bebida)


class BebidasFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput())
    precio = forms.FloatField()
    tipo = forms.ChoiceField(choices=choices_bebida)


tipo_ingrediente = Tipo_Ingrediente.objects.all()
choices_ingrediente = []
for item in tipo_ingrediente:
    choices_ingrediente.append((item.id, item.nombre))
choices_ingrediente = tuple(choices_ingrediente)


class IngredientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput())
    tipo = forms.ChoiceField(choices=choices_ingrediente)


class MesasFormulario(forms.Form):
    nSerie = forms.CharField(max_length=50, widget=forms.TextInput())


tipo_platillo = Tipo_Comida.objects.all()
choices_platillo = []
for item in tipo_platillo:
    choices_platillo.append((item.id, item.nombre))
choices_platillo = tuple(choices_platillo)


class PlatillosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput())
    descripcion = forms.CharField(max_length=50, widget=forms.Textarea())
    precio = forms.FloatField()
    tipo = forms.ChoiceField(choices=choices_platillo)


tipo_usuario = Tipo_Usuario.objects.all()
choices_usuario = []
for item in tipo_usuario:
    choices_usuario.append((item.id, item.tipo))
choices_usuario = tuple(choices_usuario)


class UsuariosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput())
    apellidos = forms.CharField(max_length=50, widget=forms.TextInput())
    nom_usuario = forms.CharField(max_length=50, widget=forms.TextInput())
    contrasena = forms.CharField(max_length=15, widget=forms.TextInput())
    tipo = forms.ChoiceField(choices=choices_usuario)
