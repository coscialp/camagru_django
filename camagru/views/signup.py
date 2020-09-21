from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from ..forms.signup import SignUpForm
from ..models import User


def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            new_user = User()
            new_user.username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            username = new_user.username
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            request.user.is_active = True
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
