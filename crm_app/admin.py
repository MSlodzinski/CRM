from django.contrib import admin

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'status', 'deadline')
    fields = ('title', 'customer__first_name', 'customer__last_name')