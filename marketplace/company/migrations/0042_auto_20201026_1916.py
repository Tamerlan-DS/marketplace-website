# Generated by Django 3.0.4 on 2020-10-26 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0041_auto_20201026_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 10, 26, 19, 16, 4, 341448), null=True),
        ),
    ]
