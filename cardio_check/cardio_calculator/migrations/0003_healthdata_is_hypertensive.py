# Generated by Django 4.2.4 on 2023-09-01 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardio_calculator', '0002_alter_healthdata_date_alter_riskscore_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthdata',
            name='is_hypertensive',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
