from django.contrib import admin
from .models import Product, ProductColor, ProductDetail, ProductImage, Cart, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "mileage", "status")
    search_fields = ("name",)
    list_filter = ("status",)


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("product", "color")
    search_fields = ("product__name", "color")


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ("product", "material")
    search_fields = ("product__name", "material")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "description")
    search_fields = ("product__name",)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "created_at", "updated_at")
    search_fields = ("user__username", "session_key")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity", "selected_color")
    search_fields = ("cart__user__username", "product__name")
