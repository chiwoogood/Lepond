from django.contrib import admin
from .models import MainImage

@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)