from django.contrib import admin
from .models import  Product, Orders, Discount, About, Client
from import_export.admin import ImportExportModelAdmin



@admin.register(Product)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "title", "description", "price", "price_type", "count", "category_data", "image", "last_update", "create_data")
    search_fields = ('title', "name")



@admin.register(Orders)
class OrdersAdmin(ImportExportModelAdmin):
    list_display = ("id", "product_id", "locatsiya", "count", "last_update", "create_data")
    search_fields = ('locatsiya',)


@admin.register(Discount)
class DiscountAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "price", "new_price", "image", "last_update", "create_data")
    search_fields = ('name', "price")



@admin.register(About)
class AboutAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "title", "image", "last_update", "create_data")
    search_fields = ('name', "title")


@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "last_update", "create_data")
    search_fields = ('name', "title")