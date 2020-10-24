from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from applications.homepage.models import Link
from applications.statistics.models import QRCode


@admin.register(Link)
class ProfileAdminModel(ModelAdmin):
    pass


@admin.register(QRCode)
class QRCodeAdminModel(ModelAdmin):
    pass
