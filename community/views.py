from django.shortcuts import render

# Create your views here.
def notice(request):
    return render(request, 'community/notice.html')

def QnA(request):
    return render(request, 'community/QnA.html')

def review(request):
    return render(request, 'community/review.html')