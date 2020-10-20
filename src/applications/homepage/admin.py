from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from applications.homepage.models import Link


@admin.register(Link)
class ProfileAdminModel(ModelAdmin):
    pass
