# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="핸드폰 번호")
    email = models.EmailField(unique=True, verbose_name="이메일")
    name = models.CharField(max_length=50, verbose_name="이름")
    bank = models.CharField(max_length=50, blank=True, null=True, verbose_name="환불 은행")
    bankAccount = models.CharField(max_length=30, blank=True, null=True, verbose_name="환불 계좌번호")
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