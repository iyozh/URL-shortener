from django.db import models

from applications.homepage.models import Link


class Hit(models.Model):
    url = models.ForeignKey(Link, on_delete=models.CASCADE, editable=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    browser = models.CharField(max_length=150, null=True, blank=True)
    os = models.CharField(max_length=150, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
