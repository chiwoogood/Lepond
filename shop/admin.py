from django.contrib import admin
from .models import Product, ProductColor, ProductDetail, ProductImage

# 색상 관리용 Inline
class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 3  # 기본으로 표시할 색상 입력 필드 수

# 상세 정보 관리용 Inline
class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 1  # 기본으로 표시할 상세 정보 입력 필드 수

# 이미지 관리용 Inline
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2  # 기본으로 표시할 이미지 입력 필드 수

# Product 관리자 페이지에서 모두 통합
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'mileage','introduce')
    search_fields = ('name',)
    inlines = [ProductColorInline, ProductDetailInline, ProductImageInline]  # 모든 Inline 추가