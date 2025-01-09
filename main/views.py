from django.shortcuts import render
from .models import MainImage
from django.contrib import messages
# Create your views here.



def main(request):
    try:
        main_image = MainImage.objects.last()
        if not main_image:
            raise MainImage.DoesNotExist("MainImage를 등록해주세요.")
    except MainImage.DoesNotExist:
        main_image = None
    context = {
        'main_image': main_image,
    }
    return render(request, 'main/main.html', context)



def about(request):
    return render(request,'main/about.html')

def agreement(request):
    return render(request,'main/agreement.html')

def policy(request):
    return render(request,'main/policy.html')
