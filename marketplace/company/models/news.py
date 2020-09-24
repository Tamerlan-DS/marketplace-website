from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    text = models.TextField(default="")
    date = models.DateTimeField(
        blank=True,
        null=True,
    )
