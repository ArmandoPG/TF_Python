# Generated by Django 4.0.3 on 2022-06-10 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionMenu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bebidas',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Mesas',
        ),
        migrations.RemoveField(
            model_name='platillos',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Bebidas',
        ),
        migrations.DeleteModel(
            name='Ingredientes',
        ),
        migrations.DeleteModel(
            name='Platillos',
        ),
        migrations.DeleteModel(
            name='Tipo_Bebida',
        ),
        migrations.DeleteModel(
            name='Tipo_Comida',
        ),
        migrations.DeleteModel(
            name='Tipo_Ingrediente',
        ),
        migrations.DeleteModel(
            name='Tipo_Usuario',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
