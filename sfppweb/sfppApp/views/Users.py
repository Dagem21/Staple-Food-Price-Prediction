import time

from django.shortcuts import render, redirect

from ..Models import User


def users(request):
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
        if user.user_type != 4:
            return redirect('/')
        else:
            users, err = user.get_users()
            usersList = []
            adminsList = []
            for u in users:
                if u.user_type == 1 or u.user_type == 2:
                    if u.user_type == 1:
                        u.user_type = 'Farmer'
                    elif u.user_type == 2:
                        u.user_type = 'Economist'
                    usersList.append(u)
                elif u.user_type == 3 or u.user_type == 4:
                    if u.user_type == 3:
                        u.user_type = 'Limited Privilege'
                    if u.user_type == 4:
                        u.user_type = 'Full Privilege'
                    adminsList.append(u)
            return render(request, 'sfppApp/users.html',
                          {'loggedIn': loggedIn, 'users': usersList, 'admins': adminsList})


def delete(request):
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
        if user.user_type != 4:
            return redirect('/')
        else:
            deleteUserid = request.GET.get('uid')
            if deleteUserid is not None:
                res = user.delete_account(deleteUserid)
                if res:
                    message = "Account deleted successfully."
                    return redirect('/users')
                else:
                    message = "Account deletion failed.Try Again!"
                    return redirect('/users')
            users, err = user.get_users()
            usersList = []
            adminsList = []
            for u in users:
                if u.user_type == 1 or u.user_type == 2:
                    if u.user_type == 1:
                        u.user_type = 'Farmer'
                    elif u.user_type == 2:
                        u.user_type = 'Economist'
                    usersList.append(u)
                elif u.user_type == 3 or u.user_type == 4:
                    if u.user_type == 3:
                        u.user_type = 'Limited Privilege'
                    if u.user_type == 4:
                        u.user_type = 'Full Privilege'
                    adminsList.append(u)
            return render(request, 'sfppApp/users.html',
                          {'loggedIn': loggedIn, 'users': usersList, 'admins': adminsList, 'delete': delete})
