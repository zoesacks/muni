# Generated by Django 4.2.5 on 2023-09-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devengados',
            name='alta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='codigo',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='emision',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='nroFactura',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='oc',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='proveedor',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='unidadEjecutora',
            field=models.TextField(blank=True),
        ),
    ]
