# Generated by Django 5.1.1 on 2024-09-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_publicacion_imagen_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='preferencias_alimenticias',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='ubicacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
