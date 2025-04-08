from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.items, name='items'),
    path('items/filter/', views.get_filtered_items, name='get_filtered_items'),
    path('details/<int:pk>/', views.details, name='details'),
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:pk>/', views.add_cart, name='add_cart'),
    path('cart/remove/<int:pk>/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
]