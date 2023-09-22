# Generated by Django 4.2.5 on 2023-09-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_alter_devengados_enviado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devengados',
            name='alta',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='emision',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='enviado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='seleccionar',
            field=models.BooleanField(default=False),
        ),
    ]