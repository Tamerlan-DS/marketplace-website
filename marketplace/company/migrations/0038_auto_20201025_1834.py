# Generated by Django 3.0.4 on 2020-10-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0037_auto_20201025_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='fake_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
