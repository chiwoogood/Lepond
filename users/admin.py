from django.contrib import admin
from .models import CustomUser, Address

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "name", "phone_number", "bank", "bankAccount")
    search_fields = ("username", "email", "name")
    list_filter = ("bank",)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "roadAddress", "jibunAddress", "extraAddress", "detailAddress", "postcode")
    search_fields = ("roadAddress", "jibunAddress", "postcode")
    list_filter = ("user",)
