from django.contrib import admin
from .models import MainImage, FooterMessage, About, Policy, Agreement
from users.admin_secure import secure_admin_site  # secure_admin_site import

class MainImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "uploaded_at")
    search_fields = ("title",)

class FooterMessageAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "uploaded_at")
    search_fields = ("title", "content")

class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title", "content")

class PolicyAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title", "content")

class AgreementAdmin(admin.ModelAdmin):
    list_display =("title", "content", "created_at")
    search_fields = ("title", "content")

# secure_admin_site에 등록
secure_admin_site.register(MainImage, MainImageAdmin)
secure_admin_site.register(FooterMessage, FooterMessageAdmin)
secure_admin_site.register(About, AboutAdmin)
secure_admin_site.register(Policy, PolicyAdmin)
secure_admin_site.register(Agreement, AgreementAdmin)
