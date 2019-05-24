from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from features.models import Features
from django.forms.models import model_to_dict
from django.contrib import messages


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
    price = 50

    feature = get_object_or_404(Features, pk=feature_id)
    feature = model_to_dict(feature, fields=['id', 'name', 'description'])
    cart = request.session.get('cart', {})
    if feature_id not in cart:
        feature.update({
            'qty': 1,
            'unit_price': price,
            'total_price': price
        })
        cart[feature_id] = feature
    else:
        cart[feature_id]['qty'] += 1
        cart[feature_id]['total_price'] = cart[feature_id]['qty'] * price
    messages.success(request, 'Successfully added item to the cart')
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('feature_archive')


@login_required()
def delete(request, feature_id):
    cart = request.session.get('cart', {})
    if feature_id in cart:
        cart.pop(feature_id)
        request.session['cart'] = cart
    messages.success(request, 'Successfully deleted item from the cart')
    return redirect(reverse('cart'))
