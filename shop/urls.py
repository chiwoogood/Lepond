from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.items, name='items'),
    path('details/<int:pk>/', views.details, name='details'),
    path('cart/', views.cart, name='cart'),
]