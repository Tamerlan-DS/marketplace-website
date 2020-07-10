# Generated by Django 3.0.3 on 2020-07-10 22:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20200707_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('ACCEPTED', 'accepted'), ('CLOSED', 'closed')], default='PENDING', max_length=255),
        ),
        migrations.AlterField(
            model_name='companyfiles',
            name='banner',
            field=models.ImageField(blank=True, upload_to='company_files/banners'),
        ),
        migrations.AlterField(
            model_name='companyfiles',
            name='picture',
            field=models.ImageField(blank=True, upload_to='company_files/pictures'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]