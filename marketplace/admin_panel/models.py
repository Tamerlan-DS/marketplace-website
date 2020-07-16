from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Card(models.Model):
    class RoleChoices(models.TextChoices):
        ADMINISTRATOR = 'ADMINISTRATOR', 'administrator'
        MODERATOR = 'MODERATOR', 'moderator'
        COMPANY_OWNER = 'COMPANY_OWNER', 'company owner'
        USER = 'USER', 'user'

    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE,
                                 related_name="card"
                                 )

    role = models.CharField(max_length=255,
                            choices=RoleChoices.choices,
                            default=RoleChoices.USER,
                            )
