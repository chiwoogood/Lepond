from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="핸드폰 번호")
    email = models.EmailField(unique=True, verbose_name="이메일")
    name = models.CharField(max_length=50, verbose_name="이름")
    mileage = models.PositiveIntegerField(default=0, verbose_name="마일리지")
    refund_bank = models.CharField(max_length=50, blank=True, null=True, verbose_name="환불 은행")
    refund_account_number = models.CharField(max_length=30, blank=True, null=True, verbose_name="환불 계좌번호")

    def __str__(self):
        return self.username

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="addresses", verbose_name="사용자")
    address_line1 = models.CharField(max_length=255, verbose_name="주소 1")
    address_line2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="주소 2")
    city = models.CharField(max_length=100, verbose_name="도시")
    state = models.CharField(max_length=100, verbose_name="주/도")
    postal_code = models.CharField(max_length=20, verbose_name="우편번호")

    def __str__(self):
        return f"{self.address_line1}, {self.city}, {self.country}"
