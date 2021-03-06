# Generated by Django 3.1.1 on 2021-02-13 19:27

import app.appmain1registration.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain1registration', '0002_auto_20210210_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user__username']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=app.appmain1registration.models.custom_upload_to),
        ),
        migrations.DeleteModel(
            name='Profilelvlmod',
        ),
    ]
