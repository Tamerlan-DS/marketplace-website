from django.db import models
from .company import Company
from .category import Category


class CompanyInfo(models.Model):
    company = models.OneToOneField(Company,
                                   on_delete=models.CASCADE,
                                   related_name='info',
                                   )
    name = models.CharField(max_length=255, default="")
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    categories = models.ManyToManyField(Category)
    # city =
