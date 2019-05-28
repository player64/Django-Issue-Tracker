export function checkout() {
    $('form#checkout_form').on('submit', function (e) {
        e.preventDefault();
        const form = this;
        const card = {
            number: $('#id_credit_card_number').val(),
            expMonth: $('#id_expiry_month').val(),
            expYear: $('#id_expiry_year').val(),
            cvc: $('#id_cvv').val()
        };
        Stripe.createToken(card, function (status, response) {
            if (status === 200) {
                $('.credit-card-errors').hide();
                $('#id_stripe_id').val(response.id);

                // remove credit card details
                // $('#id_credit_card_number').val('');
                // $('#id_cvv').val('');
                // $('#id_expiry_month').val('');
                // $('#id_expiry_year').val('');
                form.submit();
            } else {
                $('.credit-card-errors').text(response.error.message);
                $('#credit-card-errors').show();
            }
        });
    });
}