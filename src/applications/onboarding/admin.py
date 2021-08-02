from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from applications.onboarding.models import Profile


@admin.register(Profile)
class ProfileAdminModel(ModelAdmin):
    pass
