from django.contrib import messages
from django.shortcuts import render, redirect

from ..Forms import SettingForm
from ..Models import User


def setting(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        user = User(phone, None, None, None)
        user.get_user()
        loggedIn = True
    except KeyError as e:
        pass
    finally:
        if not loggedIn:
            return redirect('/')
        usertype = 'Farmer' if user.user_type == 1 else 'Economist'
        form = SettingForm(request.POST or None, initial={"phone_number": phone, "user_type": usertype})
        form.fields['phone_number'].disabled = True
        if user.user_type == 3 or user.user_type == 4:
            form.fields['newpass'].required = True
            form.fields['confpass'].required = True
            form.fields['user_type'].required = False
        if request.method == 'POST' and form.is_valid():
            password = form.cleaned_data.get("newpass")
            if user.user_type == 1 or user.user_type == 2:
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
                    return redirect('/setting')
            elif user.user_type == 3 or user.user_type == 4:
                res = user.update_account(password)
                if res:
                    messages.success(request, "Account updated!")
                    return redirect('/setting')
        return render(request, 'sfppApp/setting.html', {'loggedIn': loggedIn, 'usertype': user.user_type,
                                                        'form': form, 'num_notes': user.num_notifications})
