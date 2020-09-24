# Generated by Django 3.0.4 on 2020-09-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0019_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('DELETED', 'deleted')], default='DELETED', max_length=255),
        ),
    ]