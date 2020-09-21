from ..forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_func(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            raw_pwd = form.cleaned_data['password']
            user = authenticate(username=username, password=raw_pwd)
            if user:
                login(request, user)
            redirect('/')
    else:
        form = LoginForm()

    return render(request, 'signup.html', locals())
