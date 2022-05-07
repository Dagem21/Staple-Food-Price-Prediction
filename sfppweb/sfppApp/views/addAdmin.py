from django.shortcuts import render, redirect
from ..Models import User


def addAdmin(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
        return render(request, 'sfppApp/addAdmin.html', {'loggedIn': loggedIn})
    except KeyError as e:
        pass
    return render(request, 'sfppApp/addAdmin.html', {'loggedIn': loggedIn})
