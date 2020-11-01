from django.db import models
from django.urls import reverse_lazy
from storages.backends.s3boto3 import S3Boto3Storage

from applications.homepage.models import Link, upload_to


class Hit(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, editable=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    browser = models.CharField(max_length=150, null=True, blank=True)
    os = models.CharField(max_length=150, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["-time"]


class QRCode(models.Model):
    link = models.OneToOneField(Link, on_delete=models.CASCADE, primary_key=True)
    original = models.FileField(
        storage=S3Boto3Storage(), upload_to=upload_to, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "qrcode"


class UTM(models.Model):
    link = models.OneToOneField(Link, on_delete=models.CASCADE, primary_key=True)
    utm_source = models.CharField(max_length=200, null=True, blank=True)
    utm_medium = models.CharField(max_length=200, null=True, blank=True)
    utm_campaign = models.CharField(max_length=200, null=True, blank=True)
    utm_term = models.CharField(max_length=200, null=True, blank=True)
    utm_content = models.CharField(max_length=200, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("statistics:hits", kwargs={"pk": self.pk})
