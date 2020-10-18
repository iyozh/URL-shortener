from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from applications.homepage.models import Url


@admin.register(Url)
class ProfileAdminModel(ModelAdmin):
    pass
