# Generated by Django 3.1.1 on 2020-11-26 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appz1gman', '0004_auto_20201126_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registroproyecto',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='registroproyecto',
            old_name='updated',
            new_name='updated_at',
        ),
    ]