from django.contrib import admin
from .models import DeviceManagmentService
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class DeviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['site_name', 'site_type', 'serial_number']
    ordering = ['site_name']
    list_filter = ['site_name', 'site_type']
    list_display = ['site_name', 'site_type', 'serial_number']
admin.site.register(DeviceManagmentService, DeviceAdmin)
