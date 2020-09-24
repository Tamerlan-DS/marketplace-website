# Generated by Django 3.0.4 on 2020-09-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0020_reviews_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('DELETED', 'deleted'), ('PENDING', 'pending')], default='PENDING', max_length=255),
        ),
    ]