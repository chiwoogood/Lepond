from django.db import models
from users.models import CustomUser
from shop.models import Product

class QnaCategory(models.TextChoices):
    SHIPPING = 'shipping', '배송 문의'
    PAYMENT = 'payment', '결제, 환불 문의'
    PRODUCT = 'product', '제품 문의'
    OTHER = 'other', 'etc'

class Qna(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="사용자")
    category = models.CharField(max_length=20, choices=QnaCategory.choices, verbose_name="카테고리")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='qnas', 
                                verbose_name="관련 제품", null=True, blank=True)  # ✅ 변경
    title = models.CharField(max_length=255, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    
    def __str__(self):
        return self.title

class QnaInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name="공지 제목", blank=False, null=False)
    content = models.TextField(verbose_name="공지 내용", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    is_published = models.BooleanField(default=True, verbose_name="공개 여부")

    class Meta:
        verbose_name = "Q&A 공지사항"
        verbose_name_plural = "Q&A 공지사항 목록"
        ordering = ['-created_at']  # 최신 공지 먼저 표시

    def __str__(self):
        return self.title
    
class Notice(models.Model):
    title = models.CharField(max_length=255, verbose_name="공지 제목", blank=False, null=False)
    content = models.TextField(verbose_name="공지 내용", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    is_published = models.BooleanField(default=True, verbose_name="공개 여부")



# class Review(models.Model):
#     content = models.TextField(verbose_name="리뷰 내용", blank=True, Null=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
