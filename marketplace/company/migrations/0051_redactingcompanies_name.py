# Generated by Django 3.0.4 on 2020-10-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0050_redactingcompanies'),
    ]

    operations = [
        migrations.AddField(
            model_name='redactingcompanies',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
