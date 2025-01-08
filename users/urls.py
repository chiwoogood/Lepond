from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('mypage/', views.mypage, name='mypage'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    # path('logout', views.user_logout, name='logout'),
    # path('update', views.user_update, name='update'),
    # path('delete', views.user_delete, name='delete'),
]