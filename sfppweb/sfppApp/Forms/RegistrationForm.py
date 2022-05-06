from django import forms


userType = [
    ('Farmer', 'Farmer'),
    ('Economist', 'Economist'),
]


class RegistrationForm(forms.Form):
    phone_number = forms.IntegerField()
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    confpass = forms.CharField(max_length=100)
    user_type = forms.CharField(label='Account type', widget=forms.RadioSelect(choices=userType))

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        confpass = cleaned_data.get("confpass")
        usertype = cleaned_data.get("user_type")

        if len(str(phone_number)) != 9 or str(phone_number)[0] != '9':
            err = "Please provide a valid phone number!"
            raise forms.ValidationError(err)
        else:
            chars = set(r'~!@#$%^&*()-+=`?;:\|.,<>[]{}/')
            if any((c in chars) for c in username):
                err = "Special characters are not allowed in Username!"
                raise forms.ValidationError(err)
            else:
                if len(password) < 8:
                    err = "Password length must be at least 8 characters long!"
                    raise forms.ValidationError(err)
                else:
                    if password != confpass:
                        err = "Passwords do not match!"
                        raise forms.ValidationError(err)
        return cleaned_data
