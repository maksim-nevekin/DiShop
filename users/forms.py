from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    
    class Meta:
        model = User
    
    username = forms.CharField()    
    password = forms.CharField()
    
    # username = forms.CharField(label='Введите имя пользователя',
    #     widget=forms.TextInput(
    #         attrs={
    #             "autofocus": True,
    #             "class": "form-control",
    #             "placeholder": "Введите имя пользователя",
    #         }
    #     )
    # )
    # password = forms.CharField(label='Введите пароль',
    #     strip=False,
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "autocomplete": "current-password",
    #             "class": "form-control",
    #             "placeholder": "Введите пароль",
    #         }
    #     ),
    # )

