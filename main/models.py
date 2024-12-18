from django.db import models

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class MainImage(models.Model):
    title = models.CharField(max_length=100, verbose_name="이미지 제목")
    image = ProcessedImageField(
        upload_to='main_images/',  
        processors=[ResizeToFill(800, 600)],  
        format='JPEG',  
        options={'quality': 90},
        verbose_name="메인 이미지"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="업로드 시간")

    def __str__(self):
        return self.title