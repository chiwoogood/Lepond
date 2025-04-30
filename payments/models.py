from django.db import models
from users.models import CustomUser
from shop.models import Product, ProductColor, ProductSize

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders", verbose_name="사용자", null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"{self.user.username}의 주문 ({'결제완료' if self.is_paid else '미결제'})"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    selected_color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, null=True, blank=True)
    selected_size = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30)
    payment_result = models.TextField()
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"결제 - 주문 {self.order.id}, 금액 {self.amount}원"