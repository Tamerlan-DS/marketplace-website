# Generated by Django 3.0.3 on 2020-07-23 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20200723_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='category',
            new_name='categories',
        ),
    ]
