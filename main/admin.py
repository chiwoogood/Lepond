from django.contrib import admin
from .models import MainImage, FooterMessage

@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)


@admin.register(FooterMessage)
class FooterMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','uploaded_at')
    search_fields = ('title',)