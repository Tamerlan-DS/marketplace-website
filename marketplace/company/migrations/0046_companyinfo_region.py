# Generated by Django 3.0.4 on 2020-10-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0045_auto_20201026_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='region',
            field=models.TextField(default=''),
        ),
    ]