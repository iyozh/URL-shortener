from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

User = get_user_model()


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original = models.URLField(null=True, blank=True)
    shortcut = models.URLField(null=True, blank=True)
    confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "url"

    def __str__(self):
        return f"{self.shortcut}(user = {self.user})"

    def get_absolute_url(self):
        return reverse_lazy("statistics:hits", kwargs={"pk": self.pk})
