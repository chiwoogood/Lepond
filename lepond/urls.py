"""
URL configuration for lepond project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from users.admin_secure import secure_admin_site
from two_factor.urls import urlpatterns as tf_urls


def custom_404_test_view(request):
    return render(request, '404.html', status=404)

def custom_500_test_view(request):
    return render(request, '500.html', status=500)


urlpatterns = [
    path('secure-login/', include(tf_urls)), 
    path('admin/', secure_admin_site.urls),  
    path('', include(('main.urls', 'main'), namespace='main')),
    path('users/', include(('users.urls', 'users'), namespace='users')), 
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')), 
    path('community/', include(('community.urls', 'community'), namespace='community')),
    path('payments/',include(('payments.urls', 'payments'), namespace='payments')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)