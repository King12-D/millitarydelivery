from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'receiver_name', 'address', 'location', 'status', 'created_at')
    search_fields = ('receiver_name', 'tracking_id', 'address', 'location')
    ordering = ('-created_at',)
    list_editable = ('location',)  # Allows updating location directly in admin list view
