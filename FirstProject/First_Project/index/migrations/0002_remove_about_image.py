# Generated by Django 3.2.4 on 2021-06-30 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='image',
        ),
    ]
