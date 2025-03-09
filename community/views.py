from django.shortcuts import render, redirect, get_object_or_404
from .models import QnaCategory, Qna, QnaInfo, Notice
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden


def notice(request):
    notices = Notice.objects.all()

    context = {
        "notices" : notices,
    }
    return render(request, 'community/notice.html', context)

def notice_detail(request, pk):
    
    return render(request, 'community/notice_detail.html')


def QnA(request):
    page = request.GET.get('page', 1) 
    qna_list = Qna.objects.all().order_by('-created_at')  
    qna_info_list = QnaInfo.objects.all().order_by('-created_at') 

    paginator = Paginator(qna_list, 10)  
    qna_page = paginator.get_page(page)  

    context = {
        "QnAs": qna_page,  
        "QnaInfos": qna_info_list,
    }
    return render(request, 'community/QnA.html', context)

@login_required
def QnA_form(request):
    if request.method == 'POST': 
        category = request.POST.get("category")
        product_id = request.POST.get("product")
        title = request.POST.get("title")
        content = request.POST.get("content")

        if category == QnaCategory.PRODUCT and not product_id:
            messages.error(request, "제품을 선택하세요.")
            return render(request, "community/qna_form.html", {
                "QnaCategory": QnaCategory,
                "products": Product.objects.all(),
                "category": category,
                "title": title,
                "content": content,
            })

        if category in [QnaCategory.SHIPPING, QnaCategory.OTHER, QnaCategory.PAYMENT]:
            product = None
        else:
            product = get_object_or_404(Product, id=product_id)


        if not category or not title or not content:
            messages.error(request, "모든 필드를 입력하세요.")
            return render(request, "community/qna_form.html", {
                "QnaCategory": QnaCategory,
                "products": Product.objects.all(),
                "category": category,
                "product_id": product_id,
                "title": title,
                "content": content,
            })

        Qna.objects.create(
            user=request.user,
            category=category,
            product=product,
            title=title,
            content=content
        )
        messages.success(request, "QnA가 성공적으로 등록되었습니다.")
        return redirect('community:QnA') 
    product_list = Product.objects.all()
    context = {
        "QnaCategory" : QnaCategory,
        "products" : product_list,
    }
    return render(request, "community/QnA_form.html", context)

 
@login_required
def QnA_detail(request, pk):
    qna = get_object_or_404(Qna, pk=pk)

    # 게시글 작성자 또는 관리자만 접근 가능
    if not (request.user == qna.user or request.user.is_superuser):
        messages.error(request, "접근 권한이 없습니다.")
        return redirect('community:QnA')  # 게시글 목록 페이지로 이동

    return render(request, 'community/qna_detail.html', {'qna': qna})

def review(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'community/review.html')

def review_form(request):
    return render(request, 'community/review_form.html')



