# Generated by Django 4.0.6 on 2022-08-27 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_core', '0002_contact_photo_owner_alter_photo_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='coloring',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='renovation',
        ),
    ]
