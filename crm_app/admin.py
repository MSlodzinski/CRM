from django.contrib import admin
from .models import Order, Customer

# Register your models here.

admin.site.register(Customer)   
admin.site.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'status', 'deadline')
    fields = ('title', 'customer__first_name', 'customer__last_name')