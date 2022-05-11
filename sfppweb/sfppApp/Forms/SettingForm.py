from django import forms

from ..Models import User

userType = [
    ('Farmer', 'Farmer'),
    ('Economist', 'Economist'),
]


class SettingForm(forms.Form):
    phone_number = forms.IntegerField(label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100, label="Password")
    newpass = forms.CharField(widget=forms.PasswordInput(), max_length=100, label="New Password", required=False)
    confpass = forms.CharField(widget=forms.PasswordInput(), max_length=100, label="Confirm Password", required=False)
    user_type = forms.CharField(label='Account type', widget=forms.RadioSelect(choices=userType))

    def clean(self):
        cleaned_data = super().clean()
        phonenum = cleaned_data.get("phone_number")
        password = cleaned_data.get("password")
        newpass = cleaned_data.get("newpass")
        confpass = cleaned_data.get("confpass")

        user = User(phonenum, None, password, None)
        auth_user, err = user.login()
        if err is None:
            if len(newpass) != 0:
                if len(confpass) != 0:
                    if len(newpass) < 8:
                        err = "Password length must be at least 8 characters long!"
                        raise forms.ValidationError(err)
                    else:
                        if newpass != confpass:
                            err = "Passwords do not match!"
                            raise forms.ValidationError(err)
                else:
                    err = "Confirm your new password!"
                    raise forms.ValidationError(err)

        else:
            err = "The password provided is incorrect!"
            raise forms.ValidationError(err)
        return cleaned_data
