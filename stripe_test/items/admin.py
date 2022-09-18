from django.contrib import admin

from .models import Item, Order, Discount


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'currency')
    list_filter = ('id', 'name', 'price', 'currency')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'sum_price', 'discount')
    list_filter = ('id',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'percent_off')
    list_filter = ('id', 'percent_off')
