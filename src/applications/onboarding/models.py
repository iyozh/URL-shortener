from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    location = CountryField()
    birth_date = models.DateField()

    class Meta:
        verbose_name_plural = "profile"

    def __str__(self):
        return f"{self.user.username}"
