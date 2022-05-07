from django import forms


class LoginForm(forms.Form):
    phone_number = forms.IntegerField()
    password = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")

        if len(str(phone_number)) != 9 or str(phone_number)[0] != '9':
            err = "Please provide a valid phone number!"
            raise forms.ValidationError(err)
        return cleaned_data