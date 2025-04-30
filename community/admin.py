from django.contrib import admin
from .models import Qna, QnaInfo, Notice, Review, ReviewImage, ReviewComment

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


class ReviewCommentInline(admin.TabularInline):
    model = ReviewComment
    fields = ("content", "created_at")
    readonly_fields = ("created_at",)
    extra = 1
    
class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    fields = ("image", "description")
    readonly_fields = ()
    extra = 0 

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "title", "rating", "created_at")
    search_fields = ("title", "content", "user__username", "product__name")
    list_filter = ("created_at",)
    inlines = [ReviewImageInline, ReviewCommentInline]


@admin.register(ReviewImage)
class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ("review", "image", "description")
    search_fields = ("review__title", "description")

