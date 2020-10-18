from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original = models.URLField(null=True, blank=True)
    shortcut = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "url"

    def __str__(self):
        return f"{self.shortcut}(user = {self.user})"
