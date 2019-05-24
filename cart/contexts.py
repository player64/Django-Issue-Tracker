
def number_items_in_cart(request):
    """
    It's returns number of items in the cart this file needs to be added in
    settings.py -> TEMPLATES -> OPTIONS -> context_processors
    """
    cart = request.session.get('cart', {})
    return {'cart_items': len(cart.keys()) if cart.keys() else 0}
