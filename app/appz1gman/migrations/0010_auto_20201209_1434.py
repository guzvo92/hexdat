# Generated by Django 3.1.1 on 2020-12-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appz1gman', '0009_auto_20201130_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroproyecto',
            name='category',
        ),
        migrations.RemoveField(
            model_name='registroproyecto',
            name='mainimage',
        ),
        migrations.AddField(
            model_name='registroproyecto',
            name='details',
            field=models.CharField(default='null', max_length=500),
        ),
    ]
