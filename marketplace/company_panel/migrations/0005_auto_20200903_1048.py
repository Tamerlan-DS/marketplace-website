# Generated by Django 3.0.3 on 2020-09-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_panel', '0004_auto_20200903_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='reason',
            field=models.CharField(default='Undefined', max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(default='Undefined', max_length=255),
        ),
    ]