from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
    )
    delivery_address = forms.CharField(required=False)
    delivery_price = forms.CharField(required=False)
    requires_installment = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
    )
    installment = forms.ChoiceField(
        choices=[
            ("0"),
            ("1"),
            ("2"),
            ("3"),
        ],
    )
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
    )



