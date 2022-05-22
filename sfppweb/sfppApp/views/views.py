from django.shortcuts import render, redirect
from django.contrib import messages
from dateutil.relativedelta import relativedelta
from ..Forms import RegistrationForm, LoginForm
from ..Models import User, Predictions


def welcome(request):
    loggedIn = False
    try:
        predictions = Predictions.view_predictions()
        first_month = predictions[0].firstMonth
        month = get_months(first_month)
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
        return render(request, 'sfppApp/predictions.html',
                      {'loggedIn': loggedIn, 'search': False, 'month': month, 'predictions': predictions,
                       'usertype': user.user_type, 'num_notes': user.num_notifications})
    except KeyError as e:
        pass
    except Exception as e:
        return render(request, 'sfppApp/predictions.html',
                      {'loggedIn': loggedIn, 'search': False})
    return render(request, 'sfppApp/predictions.html',
                  {'loggedIn': loggedIn, 'search': False, 'month': month, 'predictions': predictions})


def search(request):
    loggedIn = False
    try:
        user_type = None
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
        user_type = user.user_type
    except KeyError as e:
        pass
    finally:
        query = request.GET.get('search')
        chars = set(r'~!@#$%^&*()-+=`?;:\|.,<>[]{}/')
        if any((c in chars) for c in query):
            predictions = []
        else:
            predictions = Predictions.search_food(None, query)
        if len(predictions) != 0:
            first_month = predictions[0].firstMonth
            month = get_months(first_month)
            return render(request, 'sfppApp/predictions.html',
                          {'loggedIn': loggedIn, 'search': True, 'month': month, 'predictions': predictions,
                           'usertype': user_type})
        else:
            return render(request, 'sfppApp/predictions.html',
                          {'loggedIn': loggedIn, 'search': True, 'usertype': user_type})


def get_months(first_month):
    months = [first_month.strftime('%B, %Y'), (first_month + relativedelta(months=1)).strftime('%B, %Y'),
             (first_month + relativedelta(months=2)).strftime('%B, %Y'),
             (first_month + relativedelta(months=3)).strftime('%B, %Y'),
             (first_month + relativedelta(months=4)).strftime('%B, %Y'),
             (first_month + relativedelta(months=5)).strftime('%B, %Y')]
    return months


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
