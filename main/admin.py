from django.contrib import admin
from .models import MainImage, FooterMessage, About, Policy, Agreement

@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "uploaded_at")
    search_fields = ("title",)


@admin.register(FooterMessage)
class FooterMessageAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "uploaded_at")
    search_fields = ("title", "content")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title", "content")


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title", "content")

@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display =("title", "content", "created_at")
    search_fields = ("title", "content")
