# Generated by Django 3.0.4 on 2020-09-28 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0025_uslugi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='company',
        ),
        migrations.AddField(
            model_name='services',
            name='company_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='company.Company'),
            preserve_default=False,
        ),
    ]
