from django import forms

from ..Models import User

userType = [
    ('Farmer', 'Farmer'),
    ('Economist', 'Economist'),
]


class SettingForm(forms.Form):
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': "form-control",
                'id': "phone-number"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'id': "oldpass",
                'data-cy': 'old-password'
            }
        ),
        max_length=100
    )
    newpass = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'id': "newpass",
                'data-cy': 'new-password'
            }
        ),
        max_length=100
        , required=False
    )
    confpass = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'id': "confpass",
                'data-cy': 'confirm-password'
            }
        ),
        max_length=100,
        required=False
    )
    user_type = forms.CharField(
        widget=forms.Select(
            choices=userType,
            attrs={
                'class': "form-select",
                'id': 'usertype',
                'data-cy': 'usertype'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        phonenum = cleaned_data.get("phone_number")
        password = cleaned_data.get("password")
        newpass = cleaned_data.get("newpass")
        confpass = cleaned_data.get("confpass")
        userType = cleaned_data.get("user_type")

        user = User(phonenum, None, password, None)
        auth_user, err = user.login()
        if err is None:
            if len(newpass) != 0:
                if newpass == password:
                    err = "Your new password should be different from the old one!"
                    raise forms.ValidationError({'newpass': err})
                else:
                    if len(confpass) != 0:
                        if len(newpass) < 8:
                            err = "Password length must be at least 8 characters long!"
                            raise forms.ValidationError({'newpass': err})
                        else:
                            if newpass != confpass:
                                err = "Passwords do not match!"
                                raise forms.ValidationError({'confpass': err})
                    else:
                        err = "Confirm your new password!"
                        raise forms.ValidationError({'confpass': err})
            else:
                if userType == "Economist" and user.user_type == 2:
                    err = "Please enter a new password!"
                    raise forms.ValidationError({'newpass': err})
                elif userType == "Farmer" and user.user_type == 1:
                    err = "Please enter a new password!"
                    raise forms.ValidationError({'newpass': err})
        else:
            err = "The password provided is incorrect!"
            raise forms.ValidationError({'password': err})
        return cleaned_data
