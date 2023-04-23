from django.db import models

# Create your models here.


class Notes(models.Model):
    title = models.CharField(max_length=255)
    date_change = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    favorite = models.BooleanField(default=False)
