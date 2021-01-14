from django.contrib import admin
from home.models import Location, Manufacturer, Inventory, Product, Shop, Order


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "location"]


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["arrived_at", "product", "quantity"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "manufacturer", "stock_price", "retail_price", "stock"]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "shopkeeper_name", "location"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["shop", "product", "quantity", "amount"]
