from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
from .models import Product, Cart, CartItem, ProductCategory
from community.models import Review, Qna
from django.contrib import messages


def items(request):
    categories = ProductCategory.objects.all()
    products_list = Product.objects.filter(is_active=True).order_by('-created_at')
    paginator = Paginator(products_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    quantities = {}
    for product in products:
        product_quantities = []
        for q in product.quantities.select_related('color', 'size'):
            if q.color and q.size:
                product_quantities.append({
                    'color': str(q.color.id),
                    'size': str(q.size.id),
                    'stock': q.stock
                })
        quantities[str(product.id)] = product_quantities

    context = {
        'products': products,
        'categories': categories,
        'quantities': quantities,
    }
    return render(request, 'shop/items.html', context)

@require_GET
def get_filtered_items(request):
    category_id = request.GET.get('category')
    products_list = Product.objects.filter(is_active=True).order_by('-created_at')

    if category_id:
        try:
            category_id = int(category_id)
            products_list = products_list.filter(category_id=category_id).order_by('-created_at')
        except ValueError:
            pass

    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    product_ids = [product.id for product in products]
    return JsonResponse({'product_ids': product_ids})

def details(request, pk):
    product = get_object_or_404(Product, pk=pk)

    quantities_qs = product.quantities.select_related('color', 'size')
    quantities = [
        {
            'color': str(q.color.id),
            'size': str(q.size.id),
            'stock': q.stock
        }
        for q in quantities_qs
    ]

    review_qs = Review.objects.filter(product=product).order_by('-created_at')
    qna_qs = Qna.objects.filter(product=product).order_by('-created_at')

    context = {
        'product': product,
        'quantities': quantities,
        'reviews': review_qs[:5],
        'qnas': qna_qs[:5],
        'review_count': review_qs.count(),
        'qna_count': qna_qs.count(),
    }

    return render(request, 'shop/details.html', context)



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

    return redirect(request.POST.get('next', 'shop:items'))

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