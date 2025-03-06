from django.contrib import admin
from .models import Qna, QnaInfo, Notice

@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'product', 'created_at')  # 목록에서 표시할 필드
    search_fields = ('title', 'content', 'user__username', 'product__name')  # 검색 필드
    list_filter = ('category', 'created_at')  # 필터 기능 추가
    ordering = ('-created_at',)  # 최신순 정렬


@admin.register(QnaInfo)
class QnaInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at', 'updated_at')  # 목록에서 보이는 필드
    search_fields = ('title', 'content')  # 검색 가능 필드
    list_filter = ('is_published', 'created_at')  # 필터 추가
    ordering = ('-created_at',)  # 최신 순 정렬

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)