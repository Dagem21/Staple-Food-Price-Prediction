from django.shortcuts import render, redirect
from django.contrib import messages

from ..Forms.AddAdminForm import AddAdminForm
from ..Models import User


def addAdmin(request):
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
        if user.user_type != 4:
            error = "You don't have the appropriate authorization to access this page."
            return redirect('/')
        form = AddAdminForm(request.POST or None)

        err = ''
        if request.method == 'POST' and form.is_valid():
            phonenum = form.cleaned_data.get("phone_number")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            selected = form.cleaned_data.get("admin_privileges")
            admin_privileges = 3
            if selected:
                admin_privileges = 4
            user = User(phonenum, username, password, admin_privileges)
            res, err = user.signup()
            if res:
                messages.success(request, "Admin registered successfully!")
        return render(request, 'sfppApp/addAdmin.html', {'loggedIn': loggedIn, 'form': form, 'error': err})
