from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from features.models import Features
from django.forms.models import model_to_dict
from django.contrib import messages

FEATURE_PRICE = 50


@login_required()
def view(request):
    """
    display content of the cart
    """
    cart = request.session.get('cart', {})
    cart_items = [cart[item] for item in cart.keys()] if cart.keys() else []
    return render(request, 'cart.html', {'cart': cart_items})


@login_required()
def add(request, feature_id):
    """
    Ensure feature exists to add it to the cart
    """

    feature = get_object_or_404(Features, pk=feature_id)
    feature = model_to_dict(feature, fields=['id', 'name', 'description'])
    cart = request.session.get('cart', {})

    if feature_id not in cart:
        feature.update({
            'qty': 1,
            'unit_price': FEATURE_PRICE,
            'total_price': FEATURE_PRICE
        })
        cart[feature_id] = feature
    else:
        cart[feature_id]['qty'] += 1
        cart[feature_id]['total_price'] = cart[feature_id]['qty'] * FEATURE_PRICE

    request.session['cart'] = cart
    calculate_total_price(request)

    messages.success(request, 'Successfully added item to the cart')

    request.session.modified = True
    return redirect('cart')


@login_required()
def adjust(request, action, feature_id):
    cart = request.session.get('cart', {})
    if feature_id in cart:
        adjust_qty = 1 if action == 'increment' else -1
        cart[feature_id]['qty'] += adjust_qty
        if cart[feature_id]['qty'] == 0:
            messages.success(request, 'Successfully deleted item from the cart')
            cart.pop(feature_id)
            request.session['cart'] = cart
            return redirect(reverse('cart'))
        cart[feature_id]['total_price'] = cart[feature_id]['qty'] * FEATURE_PRICE
        request.session['cart'] = cart
        calculate_total_price(request)
        messages.success(request, 'Successfully updated feature quantity')
        request.session.modified = True
    return redirect(reverse('cart'))


@login_required()
def delete(request, feature_id):
    cart = request.session.get('cart', {})
    if feature_id in cart:
        cart.pop(feature_id)
        request.session['cart'] = cart
    calculate_total_price(request)
    messages.success(request, 'Successfully deleted item from the cart')
    request.session.modified = True
    return redirect(reverse('cart'))


def calculate_total_price(request):
    cart = request.session.get('cart', {})
    # adjust total price
    cart_total_price = 0
    for item in cart:
        cart_total_price += cart[item]['total_price']
    request.session['cart_total_price'] = cart_total_price
    request.session.modified = True
