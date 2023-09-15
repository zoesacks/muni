# Generated by Django 4.2.5 on 2023-09-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cuadroPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('nroFactura', models.CharField(max_length=30)),
                ('proveedor', models.CharField(max_length=70)),
                ('oc', models.CharField(max_length=30)),
                ('factura', models.CharField(max_length=30)),
                ('ff', models.CharField(max_length=10)),
                ('unidadEjecutora', models.CharField(max_length=10)),
                ('objeto', models.TextField()),
            ],
            options={
                'verbose_name': 'devengados',
            },
        ),
    ]
