from django.contrib import admin
from .models import DeviceManagment
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class DeviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['site_name', 'user_name', 'user_number']
    ordering = ['site_name']
    list_filter = ['site_name', 'user_name']
    list_display = ['site_name', 'user_name', 'user_number']
admin.site.register(DeviceManagment, DeviceAdmin)
