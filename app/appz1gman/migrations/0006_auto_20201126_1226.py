# Generated by Django 3.1.1 on 2020-11-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appz1gman', '0005_auto_20201126_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroproyecto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
