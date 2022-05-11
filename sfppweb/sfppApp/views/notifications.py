from django.shortcuts import render, redirect
from ..Models import User, Notification


def notifications(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
        return render(request, 'sfppApp/notifications.html', {'loggedIn': loggedIn})
    except KeyError as e:
        pass
    finally:
        if not loggedIn:
            return redirect('/login')
        if user.user_type != 2:
            return redirect('/')
        notifications = user.notifications()
        return render(request, 'sfppApp/notifications.html', {'loggedIn': loggedIn, 'notifications': notifications})
