from django.contrib import admin
from .models import DeviceManagment

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    search_fields = ['site_name', 'user_name', 'user_number']
    ordering = ['site_name']
    list_filter = ['site_name', 'user_name']
    list_display = ['site_name', 'user_name', 'user_number']
admin.site.register(DeviceManagment, DeviceAdmin)