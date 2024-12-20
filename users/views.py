from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request, 'users/signin.html')


def mypage(request):
    return render(request, 'users/mypage.html')