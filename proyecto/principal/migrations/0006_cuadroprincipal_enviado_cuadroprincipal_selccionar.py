# Generated by Django 4.2.5 on 2023-09-20 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_cuadroprincipal_objeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadroprincipal',
            name='enviado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cuadroprincipal',
            name='selccionar',
            field=models.BooleanField(default=False),
        ),
    ]