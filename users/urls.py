from django.urls import path
from . import views

app_name = 'users'  # 네임스페이스 설정

urlpatterns = [
    path('login/', views.login, name='login'),
]