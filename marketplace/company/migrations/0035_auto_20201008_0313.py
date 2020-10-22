# Generated by Django 3.0.4 on 2020-10-07 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0034_companyinfo_bin'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='fake_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('ACCEPTED', 'accepted'), ('CLOSED', 'closed'), ('BANNED', 'banned')], default='CLOSED', max_length=255),
        ),
    ]