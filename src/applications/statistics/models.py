from django.db import models

from applications.homepage.models import Url


class Hit(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE, editable=False)
    ip_adress = models.GenericIPAddressField(null=True, blank=True)
    browser = models.CharField(max_length=1000, null=True, blank=True)
