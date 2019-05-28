from django import forms
from .models import Order
import datetime
from .utilis import get_month_name


class PaymentForm(forms.Form):
    current_year = int(datetime.datetime.now().strftime("%Y"))
    month_choices = [(i, get_month_name(i)) for i in range(1, 13)]
    year_choices = [(i, i) for i in range(current_year, current_year+20)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label='Month', choices=month_choices)
    expiry_year = forms.ChoiceField(label='Year', choices=year_choices)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        fields = ['credit_card_number', 'cvv', 'expiry_month', 'expiry_year', 'stripe_id']


class OrderForm(forms.ModelForm):
    full_name = forms.CharField(label='Full name')
    phone_number = forms.CharField(label='Phone number')
    postcode = forms.CharField(label='Post code')
    town_or_city = forms.CharField(label='Town / City')
    street_address1 = forms.CharField(label='Street name')
    street_address2 = forms.CharField(required=False, label='Street name Line 2')
    county = forms.CharField(label='County')
    country = forms.CharField(label='Country')

    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'town_or_city', 'street_address1', 'street_address2',
                  'postcode', 'county', 'country']
