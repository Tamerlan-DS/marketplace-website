from django.db import models
from .company import Company


class Services(models.Model):
    company_services = models.ForeignKey(Company,
                                      on_delete=models.CASCADE,
                                      related_name='services',
                                      )
    company_fk = models.IntegerField(default=1)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    price = models.TextField(default="")

