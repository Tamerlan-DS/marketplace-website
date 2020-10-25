from django.db import models
from datetime import datetime

class News(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    text = models.TextField(default="")
    date = models.DateTimeField(
        default=datetime.now,
        null=True,
    )
