from django.contrib import admin
from .models import ProductCategory, Product, ProductThumbnail, ProductDetail, ProductColor, ProductSize, ProductQuantity, ProductImage, Cart, CartItem
from users.admin_secure import secure_admin_site

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

class ProductQuantityAdmin(admin.ModelAdmin):
    list_display = ("product", "color", "size", "stock")

class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "created_at", "updated_at")
    search_fields = ("user__username", "session_key")

class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "selected_color")
    search_fields = ("cart__user__username", "product__name")


secure_admin_site.register(ProductCategory, ProductCategoryAdmin)
secure_admin_site.register(Product, ProductAdmin)
secure_admin_site.register(ProductQuantity, ProductQuantityAdmin)
secure_admin_site.register(Cart, CartAdmin)
secure_admin_site.register(CartItem, CartItemAdmin)
