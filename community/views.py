from django.shortcuts import render, redirect, get_object_or_404
from .models import QnaCategory, Qna
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def notice(request):
    return render(request, 'community/notice.html')

def QnA(request):

    return render(request, 'community/QnA.html')

@login_required
def QnA_form(request):
    if request.method == 'POST': 
        category = request.POST.get("category")
        product_id = request.POST.get("product")
        title = request.POST.get("title")
        content = request.POST.get("content")
        print('hihi')
        if not category or not product_id or not title or not content:
            context = {
                "error": "모든 필드를 입력해야 합니다.",
                "QnaCategory": QnaCategory,
                "category": category,
                "product_id": product_id,
                "title": title,
                "content": content,
            }
            return render(request, "community/qna_form.html", context)

        product = get_object_or_404(Product, id=product_id)

        Qna.objects.create(
            user=request.user,
            category=category,
            product=product,
            title=title,
            content=content
        )
        messages.success(request, "QnA가 성공적으로 등록되었습니다.")
        return redirect('community:QnA') 

    context = {
        "QnaCategory": QnaCategory,
    }
    return render(request, "community/qna_form.html", context)

def review(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'community/review.html')

def review_form(request):
    return render(request, 'commuinty/review_form.html')