# Generated by Django 3.0.3 on 2020-08-15 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ADMINISTRATOR', 'administrator'), ('MODERATOR', 'moderator'), ('COMPANY_OWNER', 'company owner'), ('USER', 'user')], default='USER', max_length=255)),
                ('status', models.CharField(choices=[('ACTIVE', 'active'), ('DELETED', 'deleted')], default='ACTIVE', max_length=255)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='card', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
