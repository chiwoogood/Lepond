from django.urls import path
from . import views

app_name = 'community'  # 네임스페이스 설정

urlpatterns = [
    path('notice/', views.notice, name='notice'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),

    path('QnA/', views.QnA, name='QnA'),
    path('QnA/form/', views.QnA_form, name='QnA_form'),
    path('QnA/form/<int:pk>/', views.QnA_detail, name='QnA_info'),
    path('qna_list/<int:product_id>/', views.qna_list,name='qna_list'),

    path('review/', views.review, name='review'),
    path('review/form/', views.review_form, name='review_form'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
    path('review_list/<int:product_id>/', views.review_list, name='review_list'),
    path('review/delete/<int:pk>/', views.review_delete, name='review_delete'),

]