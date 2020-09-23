from django.db import models
from .company import Company


class CompanyInfo(models.Model):
    company = models.OneToOneField(Company,
                                   on_delete=models.CASCADE,
                                   related_name='info',
                                   )
    name = models.CharField(max_length=255, default="")
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    city = models.TextField(default="")
    phone = models.TextField(default="")
    email = models.TextField(default="")
    site = models.TextField(default="")
    worktime = models.TextField(default="")
    adress = models.TextField(default="")
