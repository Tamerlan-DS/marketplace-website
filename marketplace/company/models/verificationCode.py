from django.db import models

class VerificationCodes(models.Model):
    code = models.IntegerField(default=1)
    email = models.CharField(max_length=50, default="")