from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField

from users.models import Consult, User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    
class UserRegistrationForm(UserCreationForm):
    phone = PhoneNumberField(required = False, region='RU')

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "phone"
        )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    phone = PhoneNumberField(required = False, region='RU')


class ConsultForm(forms.ModelForm):
    phone = PhoneNumberField(region='RU')

    class Meta:
        model = Consult
        fields = ['name', 'phone']

    def __init__(self, *args, **kwargs):
        super(ConsultForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Введите ваше имя', 'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Введите номер телефона', 'class': 'form-control'})
