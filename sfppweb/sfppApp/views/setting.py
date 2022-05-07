from django.shortcuts import render, redirect
from ..Models import User


def setting(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
    except KeyError as e:
        pass
    finally:
        return render(request, 'sfppApp/setting.html', {'loggedIn': loggedIn, 'usertype': user.user_type})
