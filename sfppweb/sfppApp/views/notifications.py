import time

from django.shortcuts import render, redirect

from ..Models import User


def notifications(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        user = User(phone, None, None, None)
        user.get_user()
        loggedIn = True
        if int(time.time()) - int(request.session['time']) > 1800:
            del request.session['phone']
            del request.session['time']
            loggedIn = False
        else:
            request.session['time'] = int(time.time())
    except KeyError as e:
        print(e)
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
        if int(time.time()) - int(request.session['time']) > 1800:
            del request.session['phone']
            del request.session['time']
            loggedIn = False
        else:
            request.session['time'] = int(time.time())
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
