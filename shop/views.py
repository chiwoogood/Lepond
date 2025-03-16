from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product

def items(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 8)  
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'products' : products,
    }
    return render(request, 'shop/items.html', context)

# def QnA(request):
#     page = request.GET.get('page', 1) 
#     qna_list = Qna.objects.all().order_by('-created_at')  
#     qna_info_list = QnaInfo.objects.all().order_by('-created_at') 

#     paginator = Paginator(qna_list, 10)  
#     qna_page = paginator.get_page(page)  

#     context = {
#         "QnAs": qna_page,  
#         "QnaInfos": qna_info_list,
#     }
#     return render(request, 'community/QnA.html', context)


def details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product' : product
    }
    return render(request, 'shop/details.html',context)

def cart(request):
    return render(request, 'shop/cart.html')


