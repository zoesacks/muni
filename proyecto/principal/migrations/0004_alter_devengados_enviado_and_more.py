# Generated by Django 4.2.5 on 2023-09-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_alter_devengados_codigo_alter_devengados_ff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devengados',
            name='enviado',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='devengados',
            name='seleccionar',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
