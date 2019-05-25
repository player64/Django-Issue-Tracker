
def number_items_in_cart(request):
    """
    It's returns number of items in the cart this file needs to be added in
    settings.py -> TEMPLATES -> OPTIONS -> context_processors
    """
    cart = request.session.get('cart', {})
    cart_total_price = request.session.get('cart_total_price', 0)
    return {
        'cart_items': len(cart.keys()) if cart.keys() else 0,
        'cart_total_price': cart_total_price
    }
