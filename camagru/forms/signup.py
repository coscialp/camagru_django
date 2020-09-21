from django import forms
from django.utils.translation import ugettext_lazy as _
from ..models import User


class SignUpForm(forms.ModelForm):

    username = forms.CharField(
        label=_("username"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'required': 'true',
                                      'placeholder': 'Username',
                                      'style': 'margin-bottom: 7%'
                                      }),
        help_text=_("Enter user Username.")
    )

    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',
                                          'placeholder': 'Password',
                                          'style': 'margin-bottom: 7%',
                                          })
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          'placeholder': 'Confirm your password',
                                          'style': 'margin-bottom: 7%'
                                          }),
        help_text=_("Enter the same password as above, for verification.")
    )

    first_name = forms.CharField(
        label=_("first name"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'required': 'true',
                                      'placeholder': 'First Name',
                                      'style': 'margin-bottom: 7%'
                                      }),
        help_text=_("Enter user first name.")
    )

    last_name = forms.CharField(
        label=_("last name"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'required': 'true',
                                      'placeholder': 'Last Name',
                                      'style': 'margin-bottom: 7%'
                                      }),
        help_text=_("Enter user first and last name.")
    )

    email = forms.CharField(
        label=_("Email"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'email',
                                      'placeholder': 'Email address',
                                      'required': 'true',
                                      'style': 'margin-bottom: 7%'
                                      })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
