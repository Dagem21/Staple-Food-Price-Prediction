from django.shortcuts import render, redirect
from django.contrib import messages
from ..Forms import SettingForm
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
        if not loggedIn:
            return redirect('/')
        usertype = 'Farmer' if user.user_type == 1 else 'Economist'
        form = SettingForm(request.POST or None, initial={"phone_number": phone, "user_type": usertype})
        form.fields['phone_number'].disabled = True
        if request.method == 'POST' and form.is_valid():
            password = form.cleaned_data.get("newpass")
            selected = form.cleaned_data.get("user_type")
            user.user_type = 1
            if selected == 'Economist':
                user.user_type = 2
            if len(password) == 0:
                res = user.update_account(None)
            else:
                res = user.update_account(password)
            if res:
                messages.success(request, "Account updated!")
                return redirect('/')

        return render(request, 'sfppApp/setting.html', {'loggedIn': loggedIn, 'usertype': user.user_type, 'form': form})
