# Generated by Django 4.1.5 on 2023-01-17 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itema',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='itemb',
            options={'ordering': ['title']},
        ),
    ]