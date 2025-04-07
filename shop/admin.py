from django.contrib import admin
from .models import ProductCategory, Product, ProductThumbnail, ProductDetail, ProductColor, ProductSize, ProductImage, Cart, CartItem

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",) 

class ProductThumbnailInline(admin.StackedInline):
    model = ProductThumbnail
    extra = 1

class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    extra = 1

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductColorInline(admin.StackedInline):
    model = ProductColor
    extra = 1

class ProductSizeInline(admin.StackedInline):
    model = ProductSize
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "mileage", "status")
    search_fields = ("name",)
    list_filter = ("status",)
    inlines = [
        ProductThumbnailInline,
        ProductDetailInline,
        ProductImageInline,
        ProductColorInline,
        ProductSizeInline,
    ]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "created_at", "updated_at")
    search_fields = ("user__username", "session_key")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "selected_color")
    search_fields = ("cart__user__username", "product__name")


