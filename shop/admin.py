from django.contrib import admin
from .models import (
    ProductCategory, Product, ProductThumbnail, ProductDetail,
    ProductColor, ProductSize, ProductQuantity, ProductImage,
    Cart, CartItem
)

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

class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 2

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "mileage")
    search_fields = ("name",)

    def get_inline_instances(self, request, obj=None):
        inlines = super().get_inline_instances(request, obj)
        if obj is None:
            return [inline for inline in inlines if not isinstance(inline, ProductQuantityInline)]
        return inlines

    inlines = [
        ProductThumbnailInline,
        ProductDetailInline,
        ProductImageInline,
        ProductColorInline,
        ProductSizeInline,
        ProductQuantityInline,
    ]

@admin.register(ProductQuantity)
class ProductQuantityAdmin(admin.ModelAdmin):
    list_display = ("product", "color", "size", "stock")

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "created_at", "updated_at")
    search_fields = ("user__username", "session_key")

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "selected_color")
    search_fields = ("cart__user__username", "product__name")
