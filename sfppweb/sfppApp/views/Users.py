from django.shortcuts import render, redirect
from ..Models import User


def users(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
        return render(request, 'sfppApp/users.html', {'loggedIn': loggedIn})
    except KeyError as e:
        pass
    return render(request, 'sfppApp/users.html', {'loggedIn': loggedIn})
