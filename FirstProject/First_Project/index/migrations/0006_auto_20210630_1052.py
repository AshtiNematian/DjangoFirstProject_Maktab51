# Generated by Django 3.2.4 on 2021-06-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_contact_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_form',
            old_name='your_name',
            new_name='full_name',
        ),
        migrations.AlterField(
            model_name='contact_form',
            name='email',
            field=models.EmailField(max_length=150),
        ),
    ]
