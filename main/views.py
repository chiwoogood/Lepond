from django.shortcuts import render
from .models import MainImage, About, Policy, Agreement
from django.contrib import messages



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
    about = About.objects.last()
    context = {
        'about' : about
    }
    return render(request,'main/about.html', context)

def agreement(request):
    agreement = Agreement.objects.last()
    context = {
        'agreement' : agreement,
    }
    return render(request,'main/agreement.html', context)

def policy(request):
    policy = Policy.objects.last()
    context = {
        'policy' : policy,
    }
    return render(request,'main/policy.html', context)




def test(request):
    return render(request, 'main/test.html')


def send_alimtalk(request):
    pass