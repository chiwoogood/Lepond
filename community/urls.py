from django.urls import path
from . import views

app_name = 'community'  # 네임스페이스 설정

urlpatterns = [
    path('notice/', views.notice, name='notice'),

    path('QnA/', views.QnA, name='QnA'),
    path('QnA/form/', views.QnA_form, name='QnA_form'),

    path('review/', views.review, name='review'),
    path('review/form/', views.review_form, name='review_form'),
]