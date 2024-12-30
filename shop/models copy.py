from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('in_stock', '재고 있음'),
        ('out_of_stock', '품절'),
        ('pre_order', '예약 주문')
    ]
    name = models.CharField(max_length=255, verbose_name="제품명")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="가격")
    mileage = models.DecimalField(max_digits=5, decimal_places=2, default=10.0, verbose_name="마일리지 (%)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_stock', verbose_name="제품 상태")
    introduce = models.CharField(max_length=255, verbose_name="상세 설명")

    def calculate_mileage_amount(self):
        return self.price * (self.mileage / 100)

    def __str__(self):
        return self.name

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors", verbose_name="제품")
    color = models.CharField(max_length=100, verbose_name="색깔")

    def __str__(self):
        return f"{self.product.name} - {self.color}"

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="details", verbose_name="제품")
    caution = models.TextField(blank=True, verbose_name="주의사항")
    material = models.CharField(max_length=255, verbose_name="소재")
    size_guide = models.TextField(blank=True, verbose_name="사이즈 가이드")
    instruction = models.TextField(blank=True, verbose_name="알림")

    def __str__(self):
        return f"{self.product.name} - 상세 정보"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="제품")
    image = models.ImageField(upload_to="product_images/", verbose_name="제품 이미지")
    description = models.CharField(max_length=255, blank=True, verbose_name="이미지 설명")

    def __str__(self):
        return f"{self.product.name} - 이미지"
