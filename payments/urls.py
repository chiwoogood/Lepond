from django.urls import path
from . import views

app_name = 'payments'  

urlpatterns = [
    path('payCenter', views.payCenter, name='payCenter'),
]