# Generated by Django 3.0.4 on 2020-10-30 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0053_auto_20201029_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='company',
        ),
    ]