# Generated by Django 3.1.1 on 2020-12-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appz1gman', '0014_auto_20201213_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroproyecto',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]