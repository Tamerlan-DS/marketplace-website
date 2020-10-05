from django.db import models


class Services(models.Model):
    company_fk = models.IntegerField(default=1)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    price = models.TextField(default="")
