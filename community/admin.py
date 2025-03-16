from django.contrib import admin
from .models import Qna, QnaInfo, Notice

@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "product", "title", "created_at", "updated_at")
    search_fields = ("title", "content", "user__username")
    list_filter = ("category", "created_at")


@admin.register(QnaInfo)
class QnaInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "updated_at")
    search_fields = ("title", "content")
    list_filter = ("is_published", "created_at")


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "updated_at")
    search_fields = ("title", "content")
    list_filter = ("is_published", "created_at")
