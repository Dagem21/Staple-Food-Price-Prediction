from django.shortcuts import render, redirect
from django.contrib import messages
from ..Forms import RegistrationForm, LoginForm
from ..Models import User


def welcome(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
    except KeyError as e:
        pass
    return render(request, 'sfppApp/predictions.html', {'loggedIn': loggedIn})


def login(request):
    form = LoginForm(request.POST or None)
    err = ''
    if request.method == 'POST' and form.is_valid():
        phonenum = form.cleaned_data.get("phone_number")
        password = form.cleaned_data.get("password")
        user = User(phonenum, None, password, None)
        auth_user, err = user.login()
        if err is None:
            request.session['phone'] = auth_user.phone_number
            messages.success(request, "Login Successful!")
            return redirect('/')
    return render(request, 'sfppApp/login.html', {'form': form, 'error': err})


def register(request):
    form = RegistrationForm(request.POST or None)
    err = ''
    if request.method == 'POST' and form.is_valid():
        phonenum = form.cleaned_data.get("phone_number")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        selected = form.cleaned_data.get("user_type")
        user_type = 1
        if selected == 'Economist':
            user_type = 2

        user = User(phonenum, username, password, user_type)
        res, err = user.signup()
        if res:
            messages.success(request, "Registration completed!")
            return redirect('/login')

    return render(request, 'sfppApp/signup.html', {'form': form, 'error': err})


def logout(request):
    if request.session['phone']:
        del request.session['phone']
    return redirect('/')

