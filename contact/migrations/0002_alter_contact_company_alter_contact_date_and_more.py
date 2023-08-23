# Generated by Django 4.1.7 on 2023-08-15 20:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="company",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Empresa"
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="date",
            field=models.DateField(default=datetime.date.today, verbose_name="Fecha"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Apellido"
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="mobile",
            field=models.CharField(max_length=12, verbose_name="Celular"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Nombre"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="notes",
            field=models.TextField(blank=True, null=True, verbose_name="Notas"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.CharField(
                blank=True, max_length=12, null=True, verbose_name="Teléfono"
            ),
        ),
    ]
