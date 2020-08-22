from django.contrib import admin
from .models import Address, Order, OrderItem


# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
