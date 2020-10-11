from django.db import models

# Create your models here.


class Url(models.Model):
    original = models.URLField(null=True, blank=True)
    shortcut = models.URLField(null=True, blank=True)
