from django.db import models

# Create your models here.
from django.urls import reverse


class Notes(models.Model):
    title = models.CharField(max_length=255)
    date_change = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_note', kwargs={'note_id': self.pk})

    class Meta:
        ordering = ['id']
