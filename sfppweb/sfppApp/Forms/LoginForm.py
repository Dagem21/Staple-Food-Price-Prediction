from django import forms
from ..Models import User


class LoginForm(forms.Form):
    phone_number = forms.IntegerField(
        label="Phone Number",
        widget=forms.NumberInput(
            attrs={
                'class': "form-control",
                'id': "phone-number",
                'data-cy': "phone-number"
            }
        )

    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'id': 'password',
                'data-cy': "password"
            }
        ),
        max_length=100,
        label="Password",
    )

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        password = cleaned_data.get("password")
        if len(str(phone_number)) != 9 or str(phone_number)[0] != '9':
            err = "Please provide a valid phone number!"
            raise forms.ValidationError(err)
        else:
            user = User(phone_number, None, password, None)
            auth_user, err = user.login()
            if err is not None:
                err = "Unknown phone number or password!"
                raise forms.ValidationError(err)
        return cleaned_data
