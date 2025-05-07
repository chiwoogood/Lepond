from django.contrib import admin
from .models import CustomUser, Address, RefundBank 

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "name", "phone_number", "marketing_agree")
    search_fields = ("username", "email", "name")

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "roadAddress", "jibunAddress", "extraAddress", "detailAddress", "postcode")
    search_fields = ("roadAddress", "jibunAddress", "postcode")
    list_filter = ("user",)

@admin.register(RefundBank)
class RefundBankAdmin(admin.ModelAdmin):
    list_display = ("user", "bank_name", "account_number")
    search_fields = ("user__username", "bank_name", "account_number")
    list_filter = ("bank_name",)
