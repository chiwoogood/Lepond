from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.signin, name='login'),
    path('mypage/', views.mypage, name='mypage'),
    path('signup/', views.user_signup, name='signup'),
    path('signin/', views.user_signin, name='signin'),
    path('signout/', views.user_signout, name='signout'),
    path('myorder/', views.myorder, name='myorder'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.user_update, name='update'),
    path('address/', views.address, name='address'),
    path('address_add/', views.user_address_add, name='address_add'),
    path('address_delete/', views.user_address_delete, name='address_delete'),
    path('mycommunity/', views.mycommunity, name='mycommunity'),
    path('test/', views.test, name='test'),
]

