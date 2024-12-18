from django.shortcuts import render

# Create your views here.

def payCenter(request):
    return render(request,'payments/payCenter.html')