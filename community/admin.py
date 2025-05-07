from django.contrib import admin
from .models import Qna, QnaInfo, Notice, Review, ReviewImage, ReviewComment
from users.admin_secure import secure_admin_site  # secure_admin_site 추가

class QnaAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "product", "title", "created_at", "updated_at")
    search_fields = ("title", "content", "user__username")
    list_filter = ("category", "created_at")

class QnaInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "updated_at")
    search_fields = ("title", "content")
    list_filter = ("is_published", "created_at")

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
    extra = 0

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "title", "rating", "created_at")
    search_fields = ("title", "content", "user__username", "product__name")
    list_filter = ("created_at",)
    inlines = [ReviewImageInline, ReviewCommentInline]

class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ("review", "image", "description")
    search_fields = ("review__title", "description")

# secure_admin_site에 모델 등록
secure_admin_site.register(Qna, QnaAdmin)
secure_admin_site.register(QnaInfo, QnaInfoAdmin)
secure_admin_site.register(Notice, NoticeAdmin)
secure_admin_site.register(Review, ReviewAdmin)
secure_admin_site.register(ReviewImage, ReviewImageAdmin)
