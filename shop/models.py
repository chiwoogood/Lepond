from django.db import models
from users.models import CustomUser

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="카테고리 이름")
    order = models.PositiveIntegerField(default=0, verbose_name="정렬 순서")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [
        ('in_stock', '재고 있음'),
        ('out_of_stock', '품절'),
        ('pre_order', '예약 주문')
    ]

    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.SET_NULL, null=True, verbose_name="카테고리")
    name = models.CharField(max_length=255, verbose_name="제품명")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="가격")
    mileage = models.DecimalField(max_digits=5, decimal_places=2, default=10.0, verbose_name="마일리지 (%)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_stock', verbose_name="제품 상태")

    def calculate_mileage_amount(self):
        return self.price * (self.mileage / 100)

    def __str__(self):
        return self.name

class ProductThumbnail(models.Model):
    product = models.ForeignKey(Product, related_name='thumbnails', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_thumbnails/", verbose_name="썸네일 이미지")

    def __str__(self):
        return f"{self.product.name} - 썸네일"



class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="details", verbose_name="제품")
    instruction = models.TextField(blank=True, verbose_name="알림")
    caution = models.TextField(blank=True, verbose_name="주의사항")
    material = models.CharField(max_length=255, verbose_name="소재")
    size_guide = models.TextField(blank=True, verbose_name="사이즈 가이드")

    def __str__(self):
        return f"{self.product.name} - 상세 정보"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="제품")
    image = models.ImageField(upload_to="product_images/", verbose_name="제품 이미지")
    description = models.CharField(max_length=255, blank=True, verbose_name="이미지 설명")

    def __str__(self):
        return f"{self.product.name} - 이미지"

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors", verbose_name="제품")
    color = models.CharField(max_length=100, verbose_name="색깔")

    def __str__(self):
        return f"{self.product.name} - {self.color}"


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="cart", verbose_name="사용자", null=True, blank=True)
    session_key = models.CharField(max_length=255, null=True, blank=True, verbose_name="세션 키")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트일")

    def __str__(self):
        if self.user:
            return f"{self.user.username}의 장바구니"
        return f"세션 {self.session_key}의 장바구니"

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items", verbose_name="장바구니")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="제품")
    selected_color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="선택한 색깔")

    def __str__(self):
        if self.cart.user:
            return f"{self.cart.user.username} - {self.product.name}"
        return f"세션 {self.cart.session_key} - {self.product.name}"

    def total_price(self):
        return self.product.price