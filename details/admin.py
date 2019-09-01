from django.contrib import admin

from .models import *


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'description', 'status']
