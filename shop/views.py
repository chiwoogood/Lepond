from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Product, Cart, CartItem, ProductCategory
from django.contrib import messages


def items(request):
    category_id = request.GET.get('category')

    products_list = Product.objects.all()
    if category_id:
        products_list = products_list.filter(category_id=category_id)

    paginator = Paginator(products_list, 8)  
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    categories = ProductCategory.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        product_data = [
            {
                "id": product.id,
                "name": product.name,
                "price": str(product.price),
                "status": product.get_status_display(),
                "thumbnail": product.thumbnails.first().image.url if product.thumbnails.exists() else ""
            } for product in products
        ]
        return JsonResponse({'products': product_data})

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/items.html', context)

def details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product' : product
    }
    return render(request, 'shop/details.html',context)

@login_required
def add_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    exists = CartItem.objects.filter(cart=cart, product=product).exists()
    if exists:
        messages.info(request, '이미 장바구니에 담긴 상품입니다.')
    else:
        CartItem.objects.create(cart=cart, product=product)
        messages.success(request, '장바구니에 상품을 담았습니다.')

    return redirect('shop:items')

@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()  
    items = cart.items.all() if cart else []  

    total_price = sum(item.total_price() for item in items)

    return render(request, 'shop/cart.html', {
        'cart': cart,
        'items': items,
        'total_price': total_price,
    })

@login_required
def remove_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    cart_item.delete()
    messages.success(request, '상품이 장바구니에서 삭제되었습니다.')
    return redirect('shop:cart')


@require_POST
@login_required
def clear_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart.items.all().delete()
        messages.success(request,'장바구니를 비웠습니다.')
    return redirect('shop:cart')