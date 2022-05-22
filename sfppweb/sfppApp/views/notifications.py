from django.shortcuts import render, redirect
from ..Models import User, Notification


def notifications(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
    except KeyError as e:
        pass
    finally:
        if not loggedIn:
            return redirect('/login')
        if user.user_type != 2:
            return redirect('/')
        notifications = user.notifications()
        return render(request, 'sfppApp/notifications.html', {'loggedIn': loggedIn, 'notifications': notifications})


def deleteNotification(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
    except KeyError as e:
        pass
    finally:
        if not loggedIn:
            return redirect('/login')
        if user.user_type != 2:
            return redirect('/')
        else:
            deleteNoti = request.GET.get('nid')
            if deleteNoti is not None:
                res = user.deleteNotification(deleteNoti)
                if res:
                    message = "Notification removed."
                else:
                    message = "Failed to remove notification. Try again!"
            return redirect('/notifications')
