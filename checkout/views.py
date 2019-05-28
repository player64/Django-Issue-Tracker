from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .forms import PaymentForm, OrderForm
from features.models import Features
from .models import OrderItem
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout_view(request):
    cart = request.session.get('cart', {})
    total_price = request.session.get('cart_total_price', 0)
    if not cart.keys() or total_price < 1:
        messages.error(request, 'Your cart is empty')
        return redirect(reverse('feature_archive'))

    cart_items = [cart[item] for item in cart.keys()]

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(total_price * 100),
                    currency='EUR',
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    order = order_form.save(commit=False)
                    order.total_price = total_price
                    order.save()
                    for feature_id in cart.keys():
                        feature = get_object_or_404(Features, pk=feature_id)
                        feature.total_votes += int(cart[feature_id]['qty'])
                        feature.voted_by.add(request.user)
                        feature.save()

                        order_item = OrderItem(
                            order=order,
                            feature=feature,
                            qty=cart[feature_id]['qty'],
                            price=cart[feature_id]['total_price']
                        )

                        order_item.save()

                    request.session['cart'] = {}
                    messages.success(request, 'You have successfully paid')
                return redirect(reverse('feature_archive'))

            except Exception as error:
                print(error)
                messages.error(request, 'Your card was declined!')
        else:
            messages.error(request, 'We were unable to take a payment with that card!')

    payment_form = PaymentForm()
    order_form = OrderForm()
    return render(request, 'checkout.html',
                  {'cart_items': cart_items, 'total_price': total_price,
                   'order_form': order_form, 'payment_form': payment_form,
                   'body_class': 'checkout',
                   'stripe_publishable': settings.STRIPE_PUBLISHABLE})
