# Generated by Django 4.1.7 on 2023-08-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0004_alter_contact_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Nombre*"),
        ),
    ]
