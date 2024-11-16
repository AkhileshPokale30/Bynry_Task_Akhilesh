# customer_service/admin.py

from django.contrib import admin
from .models import Customer, ServiceRequest

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'balance')
    search_fields = ('user__username', 'account_number')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'created_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('customer__user__username', 'customer__account_number')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
