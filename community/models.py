from django.db import models
from users.models import CustomUser
from shop.models import Product
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


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
        ordering = ['-created_at'] 

    def __str__(self):
        return self.title
    
class Notice(models.Model):
    title = models.CharField(max_length=255, verbose_name="공지 제목", blank=False, null=False)
    content = models.TextField(verbose_name="공지 내용", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    is_published = models.BooleanField(default=True, verbose_name="공개 여부")



class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="사용자")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="제품")
    title = models.CharField(max_length=255, verbose_name="리뷰 제목")
    content = models.TextField(verbose_name="리뷰 내용", blank=True, null=True)
    rating = models.PositiveIntegerField(verbose_name="평점") 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰 목록"
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.product.name}] {self.title} - {self.user.username}"
    

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="images", verbose_name="리뷰")
    image = models.ImageField(upload_to="review_images/", verbose_name="리뷰 이미지")
    description = models.CharField(max_length=255, blank=True, verbose_name="이미지 설명")

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            img.thumbnail((800, 800))

            buffer = BytesIO()
            img.save(fp=buffer, format='JPEG', quality=92)
            file_content = ContentFile(buffer.getvalue())

            self.image.save(self.image.name, file_content, save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"리뷰 ID {self.review.id} - 이미지"
    
class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments", verbose_name="리뷰")
    content = models.TextField(verbose_name="댓글 내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    class Meta:
        verbose_name = "리뷰 댓글"
        verbose_name_plural = "리뷰 댓글 목록"
        ordering = ['created_at']

    def __str__(self):
        return f"리뷰 ID {self.review.id}"