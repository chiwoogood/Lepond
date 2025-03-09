from django.contrib import admin
from .models import MainImage, FooterMessage, About, Policy

@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)


@admin.register(FooterMessage)
class FooterMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','uploaded_at')
    search_fields = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title',)