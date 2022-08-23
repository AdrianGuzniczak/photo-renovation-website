# Generated by Django 4.0.6 on 2022-08-23 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import site_core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_core', '0004_alter_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(blank=True, default=site_core.models.Photo.get_user_id, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
