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
    path('update/', views.update, name='update'),
    path('user_update/', views.user_update, name='user_update'),
    path('address/', views.address, name='address'),
    path('address/add/', views.user_address_add, name='add_address'),
    path('address/<int:pk>/edit/', views.user_address_update, name='edit_address'),
    path('address/<int:pk>/delete/', views.user_address_delete, name='delete_address'),
    path('address/<int:pk>/set-default/', views.user_address_set_default, name='set_default_address'),
    path('mycommunity/', views.mycommunity, name='mycommunity'),
    path('test/', views.test, name='test'),
]

