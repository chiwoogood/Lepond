from django.contrib import admin
from .models import CustomUser, Address, RefundBank, Mileage, Coupon
from users.admin_secure import secure_admin_site

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "name", "phone_number", "marketing_agree")
    search_fields = ("username", "email", "name")

class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "roadAddress", "jibunAddress", "extraAddress", "detailAddress", "postcode")
    search_fields = ("roadAddress", "jibunAddress", "postcode")
    list_filter = ("user",)

class RefundBankAdmin(admin.ModelAdmin):
    list_display = ("user", "bank_name", "account_number")
    search_fields = ("user__username", "bank_name", "account_number")
    list_filter = ("bank_name",)

class MileageAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "reason", "created_at")
    search_fields = ("user__username", "reason")
    list_filter = ("created_at",)

class CouponAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "discount_amount", "is_used", "expiration_date")
    search_fields = ("code", "user__username")
    list_filter = ("is_used", "expiration_date")


secure_admin_site.register(CustomUser, CustomUserAdmin)
secure_admin_site.register(Address, AddressAdmin)
secure_admin_site.register(RefundBank, RefundBankAdmin)
secure_admin_site.register(Mileage, MileageAdmin)
secure_admin_site.register(Coupon, CouponAdmin)
