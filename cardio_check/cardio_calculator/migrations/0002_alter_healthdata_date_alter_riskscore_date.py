# Generated by Django 4.2.4 on 2023-09-01 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardio_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthdata',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='riskscore',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]