# Generated by Django 3.1.1 on 2020-12-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appz1gman', '0015_auto_20201216_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalRegistroproyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=150)),
                ('details', models.CharField(default='null', max_length=500)),
                ('category', models.CharField(default='null', max_length=100)),
                ('image1', models.ImageField(default='null', upload_to='projectsgman')),
                ('image2', models.ImageField(default='null', upload_to='projectsgman')),
                ('image3', models.ImageField(default='null', upload_to='projectsgman')),
                ('image4', models.ImageField(default='null', upload_to='projectsgman')),
                ('image5', models.ImageField(default='null', upload_to='projectsgman')),
            ],
        ),
    ]
