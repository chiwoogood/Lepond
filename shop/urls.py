from django.urls import path
from . import views

app_name = 'shop'  # 네임스페이스 설정

urlpatterns = [
    path('', views.items, name='items'),
    path('details/', views.details, name='details'),
    path('cart/', views.cart, name='cart'),
]