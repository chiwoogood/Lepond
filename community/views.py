from django.shortcuts import render
from .models import QnaCategory


# Create your views here.
def notice(request):
    return render(request, 'community/notice.html')

def QnA(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'community/QnA.html')

def QnA_form(request):
    context = {
        'QnaCategory': QnaCategory
    }
    return render(request, 'community/QnA_form.html', context)

def review(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'community/review.html')

def review_form(request):
    return render(request, 'commuinty/review_form.html')