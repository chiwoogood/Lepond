from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.signin, name='login'),
    path('mypage/', views.mypage, name='mypage'),
    path('signup/', views.user_signup, name='signup'),
    path('signin/', views.user_signin, name='signin'),
    path('signout/', views.user_signout, name='signout'),
    # path('update', views.user_update, name='update'),
    # path('delete', views.user_delete, name='delete'),
]
