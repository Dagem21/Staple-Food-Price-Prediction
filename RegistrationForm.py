from django import forms

from ..Models import User

userType = [
    ('Farmer', 'Farmer'),
    ('Economist', 'Economist'),
]


class RegistrationForm(forms.Form):
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': "form-control",
                'id': "phone-number",
                'data-cy': "phone-number"
            }
        )
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'id': "username",
                'data-cy': "username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'id': 'password',
                'data-cy': 'password'
            }
        ),
        max_length=100
    )
    confpass = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'id': 'confpass',
                'data-cy': 'confirm-password'
            }
        ),
        max_length=100)
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
        phone_number = cleaned_data.get("phone_number")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        confpass = cleaned_data.get("confpass")
        usertype = cleaned_data.get("user_type")

        if len(str(phone_number)) != 9 or str(phone_number)[0] != '9':
            err = "Please provide a valid phone number!"
            raise forms.ValidationError({'phone_number': err})
        else:
            chars = set(r'~!@#$%^&*()-+=`?;:\|.,<>[]{}/')
            if any((c in chars) for c in username):
                err = "Special characters are not allowed in Username!"
                raise forms.ValidationError({'username': err})
            else:
                if len(password) < 8:
                    err = "Password length must be at least 8 characters long!"
                    raise forms.ValidationError({'password': err})
                else:
                    if password != confpass:
                        err = "Passwords do not match!"
                        raise forms.ValidationError({'confpass': err})
                    else:
                        user = User(phone_number, None, None, None)
                        exists = user.registered()
                        if exists:
                            err = "This phone number is already registered!"
                            raise forms.ValidationError({'phone_number': err})
        return cleaned_data
