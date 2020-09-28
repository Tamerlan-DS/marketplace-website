from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'pending'
        ACCEPTED = 'ACCEPTED', 'accepted'
        CLOSED = 'CLOSED', 'closed'
        BANNED = 'BANNED', 'banned'

    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE,
                                 )
    status = models.CharField(max_length=255,
                              choices=StatusChoices.choices,
                              default=StatusChoices.PENDING,
                              )
