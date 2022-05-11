from django import forms


adminType = [
    ('Limited Privileges', 'Limited Privileges'),
    ('Full Privileges', 'Full Privileges'),
]


class AddAdminForm(forms.Form):
    phone_number = forms.IntegerField(label="Phone Number")
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100, label="Password")
    confpass = forms.CharField(widget=forms.PasswordInput(), max_length=100, label="Confirm Password")
    admin_privileges = forms.CharField(label='Account type', widget=forms.RadioSelect(choices=adminType))

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        confpass = cleaned_data.get("confpass")

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
