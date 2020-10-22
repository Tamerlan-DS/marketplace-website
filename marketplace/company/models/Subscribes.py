from django.db import models


class Email(models.Model):
    email = models.EmailField(default="")
    date = models.DateTimeField(
        blank=True,
        null=True,
    )