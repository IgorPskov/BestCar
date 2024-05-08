from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_address = forms.CharField(required=False)
    delivery_price = forms.CharField(required=False)
    requires_installment = forms.ChoiceField()
    installment = forms.ChoiceField(required=False)
    payment_on_get = forms.ChoiceField()

    

