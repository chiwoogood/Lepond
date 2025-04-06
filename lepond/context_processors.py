from main.models import FooterMessage
from shop.models import Cart, ProductCategory

def global_context(request):
    try:
        footer_message = FooterMessage.objects.last()
    except FooterMessage.DoesNotExist:
        footer_message = None

    cart_item_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item_count = cart.items.count()

    try:
        category = ProductCategory.objects.all()
    except ProductCategory.DoesNotExist:
        category = None
    return {
        'footer_message': footer_message,
        'cart_item_count': cart_item_count,
        'categories' : category,
    }