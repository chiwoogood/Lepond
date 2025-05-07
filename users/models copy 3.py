from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    _phone_number = models.CharField(max_length=255, blank=True, null=True, db_column="phone_number", verbose_name="핸드폰 번호")
    email = models.EmailField(unique=True, verbose_name="이메일")
    name = models.CharField(max_length=50, verbose_name="이름")
    bank = models.CharField(max_length=50, blank=True, null=True, verbose_name="환불 은행")
    _bankAccount = models.CharField(max_length=255, blank=True, null=True, db_column="bankAccount", verbose_name="환불 계좌번호")
    marketing_agree = models.BooleanField(default=False, verbose_name="마케팅 수신 동의")

    def __str__(self):
        return self.username

    @property
    def phone_number(self):
        if self._phone_number:
            try:
                return settings.FERNET.decrypt(self._phone_number.encode()).decode()
            except Exception:
                return "[복호화 실패]"
        return None

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = settings.FERNET.encrypt(value.encode()).decode() if value else None

    @property
    def bankAccount(self):
        if self._bankAccount:
            try:
                return settings.FERNET.decrypt(self._bankAccount.encode()).decode()
            except Exception:
                return "[복호화 실패]"
        return None

    @bankAccount.setter
    def bankAccount(self, value):
        self._bankAccount = settings.FERNET.encrypt(value.encode()).decode() if value else None


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="addresses", verbose_name="사용자")

    _roadAddress = models.CharField(
        max_length=255, db_column="roadAddress", verbose_name="도로명주소"
    )
    _jibunAddress = models.CharField(
        max_length=255, blank=True, null=True, db_column="jibunAddress", verbose_name="지번주소"
    )
    _extraAddress = models.CharField(
        max_length=255, blank=True, null=True, db_column="extraAddress", verbose_name="참고주소"
    )
    _detailAddress = models.CharField(
        max_length=255, blank=True, null=True, db_column="detailAddress", verbose_name="상세주소"
    )

    postcode = models.CharField(max_length=20, verbose_name="우편번호")
    is_default = models.BooleanField(default=False, verbose_name="기본 배송지")

    def __str__(self):
        return f"{self.roadAddress} ({self.postcode})"

    @property
    def roadAddress(self):
        if self._roadAddress:
            try:
                return settings.FERNET.decrypt(self._roadAddress.encode()).decode()
            except Exception:
                return "[복호화 실패]"
        return None

    @roadAddress.setter
    def roadAddress(self, value):
        self._roadAddress = settings.FERNET.encrypt(value.encode()).decode() if value else None

    @property
    def jibunAddress(self):
        if self._jibunAddress:
            try:
                return settings.FERNET.decrypt(self._jibunAddress.encode()).decode()
            except Exception:
                return "[복호화 실패]"
        return None

    @jibunAddress.setter
    def jibunAddress(self, value):
        self._jibunAddress = settings.FERNET.encrypt(value.encode()).decode() if value else None

    @property
    def extraAddress(self):
        if self._extraAddress:
            try:
                return settings.FERNET.decrypt(self._extraAddress.encode()).decode()
            except Exception:
                return "[복호화 실패]"
        return None

    @extraAddress.setter
    def extraAddress(self, value):
        self._extraAddress = settings.FERNET.encrypt(value.encode()).decode() if value else None

    @property
    def detailAddress(self):
        if self._detailAddress:
            try:
                return settings.FERNET.decrypt(self._detailAddress.encode()).decode()
            except Exception:
                return "[복호화 실패]"
        return None

    @detailAddress.setter
    def detailAddress(self, value):
        self._detailAddress = settings.FERNET.encrypt(value.encode()).decode() if value else None
