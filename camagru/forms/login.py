from django import forms
from django.forms import TextInput


class LoginForm(forms.Form):
    username = forms.CharField(label="Username",
                               max_length=30,
                               widget=TextInput(attrs={'class': 'form-control',
                                                       'required': 'true',
                                                       'placeholder': 'Login',
                                                       'style': 'margin-bottom: 7%'
                                                       })
                               )
    password = forms.CharField(label="password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'type': 'password',
                                                                 'required': 'true',
                                                                 'placeholder': 'Password',
                                                                 'style': 'margin-bottom: 7%'
                                                                 }),
                               )
