from two_factor.admin import AdminSiteOTPRequired
from django.urls import reverse_lazy


class CustomOTPAdminSite(AdminSiteOTPRequired):
    login_url = reverse_lazy('two_factor:login')

secure_admin_site = CustomOTPAdminSite(name='secure_admin')
