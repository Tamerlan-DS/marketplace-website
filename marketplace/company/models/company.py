from django.db import models
from django.contrib.auth.models import User

class Tarif(models.Model):
    name = models.CharField(max_length=255, default="")
    price = models.FloatField(default=0)
    timeleft = models.IntegerField(default=0)
    date = models.DateField(null=True)

class Company(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'pending'
        ACCEPTED = 'ACCEPTED', 'accepted'
        CLOSED = 'CLOSED', 'closed'
        BANNED = 'BANNED', 'banned'

    charged = models.BooleanField(
        default=False,
    )
    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE,
                                 )
    status = models.CharField(max_length=255,
                              choices=StatusChoices.choices,
                              default=StatusChoices.CLOSED,
                              )

class CompanyTarif(models.Model):
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name="tarifes",
                                )
    tarif = models.ForeignKey(Tarif,
                                 on_delete=models.CASCADE,
                                 related_name="companiees",
                                 )
