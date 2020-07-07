from django.db import models
from .company import Company


class CompanyInfo(models.Model):
    company = models.OneToOneField(Company,
                                   on_delete=models.CASCADE,
                                   )
    name = models.CharField(max_length=255, default="")
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    # tags =
    # city =
