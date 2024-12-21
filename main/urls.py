from django.urls import path
from . import views

app_name = 'main'  # 네임스페이스 설정

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('agreement/', views.agreement, name='agreement'),
    path('baba/', views.babo, name='babo'),
]