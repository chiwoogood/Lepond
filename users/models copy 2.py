from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="핸드폰 번호")
    email = models.EmailField(unique=True, verbose_name="이메일")
    name = models.CharField(max_length=50, verbose_name="이름")
    marketing_agree = models.BooleanField(default=False, verbose_name="마케팅 수신 동의")

    def __str__(self):
        return self.username


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="addresses", verbose_name="사용자")
    roadAddress = models.CharField(max_length=255, verbose_name="도로명주소")
    jibunAddress = models.CharField(max_length=255, blank=True, null=True, verbose_name="지번주소")
    extraAddress = models.CharField(max_length=255, blank=True, null=True, verbose_name="참고주소")
    detailAddress = models.CharField(max_length=255, blank=True, null=True, verbose_name="상세주소")
    postcode = models.CharField(max_length=20, verbose_name="우편번호")

    def __str__(self):
        return f"{self.roadAddress} ({self.postcode})"


class RefundBank(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='refund_account', verbose_name="사용자")
    bank_name = models.CharField(max_length=50, verbose_name="은행명")
    account_number = models.CharField(max_length=30, verbose_name="계좌번호")

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"
    

class Mileage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mileage_logs', verbose_name="사용자")
    amount = models.IntegerField(verbose_name="변동 마일리지")
    reason = models.CharField(max_length=255, blank=True, null=True, verbose_name="사유")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="변경 일시")

    def __str__(self):
        return f"{self.user.username} / {self.amount}P"


class Coupon(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='coupons', verbose_name="사용자")
    code = models.CharField(max_length=20, unique=True, verbose_name="쿠폰 코드")
    discount_amount = models.PositiveIntegerField(verbose_name="할인 금액")
    is_used = models.BooleanField(default=False, verbose_name="사용 여부")
    expiration_date = models.DateField(verbose_name="유효기간")

    def __str__(self):
        return f"{self.code} - {'사용됨' if self.is_used else '미사용'}"