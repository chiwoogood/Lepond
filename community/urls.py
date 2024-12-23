from django.urls import path
from . import views

app_name = 'community'  # 네임스페이스 설정

urlpatterns = [
    path('', views.notice, name='notice'),
    path('QnA',views.QnA, name='QnA'),
    path('review/', views.review, name='review'),
]