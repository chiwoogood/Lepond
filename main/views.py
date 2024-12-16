from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request,'main/main.html')


def agreement(request):
    return render(request,'main/agreement.html')

def policy(request):
    return render(request,'main/policy.html')