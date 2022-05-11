from django import forms
from ..Database import databse


class DateInput(forms.DateInput):
    input_type = 'date'


dataTypes = [
    ('Food Price', 'Food Price'),
    ('Weather Data', 'Weather Data'),
    ('Fuel Data', 'Fuel Data'),
    ('Exchange Rate Data', 'Exchange Rate Data')]
dataItems = [
    ('Precipitation', 'Precipitation'),
    ('Diesel Price', 'Diesel Price'),
    ('Petrol Price', 'Petrol Price'),
    ('Exchange Rate', 'Exchange Rate')]


class AddDataForm(forms.Form):
    foodNames, err = databse.getFoodNames()
    foodList = []
    for food in foodNames:
        option = (food, food)
        foodList.append(option)
    combined = dataItems + foodList
    locations, err = databse.getLocations()
    locationsList = []
    for location in locations:
        option = (location, location)
        locationsList.append(option)
    month = forms.DateField(
        widget=DateInput()
    )
    location = forms.CharField(
        widget=forms.Select(choices=locationsList),
        label="Location"
    )
    dataType = forms.CharField(
        widget=forms.Select(choices=dataTypes),
        label="Type of Data",
    )
    dataItem = forms.CharField(
        widget=forms.Select(choices=combined),
        label="Data Item"
    )
    value = forms.DecimalField(
        label="Value"
    )

    def clean(self):
        cleaned_data = super().clean()
        month = cleaned_data.get("month")
        location = cleaned_data.get("location")
        dataType = cleaned_data.get("dataType")
        dataItem = cleaned_data.get("dataItem")

        chars = set(r'~!@#$%^&*()+=`?;:\|.<>[]{}/')
        if any((c in chars) for c in location):
            err = "Special characters are not allowed in Location!"
            raise forms.ValidationError(err)
        else:
            if any((c in chars) for c in dataType):
                err = "Special characters are not allowed in Type of Data!"
                raise forms.ValidationError(err)
            else:
                if any((c in chars) for c in dataItem):
                    err = "Special characters are not allowed in Data Item!"
                    raise forms.ValidationError(err)
        if dataType == 'Weather Data':
            if dataItem != 'Precipitation':
                err = "Data item doesn't fit with the selected data type!"
                raise forms.ValidationError(err)
        elif dataType == 'Fuel Data':
            if dataItem != 'Diesel Price' and dataItem != 'Petrol Price':
                err = "Data item doesn't fit with the selected data type!"
                raise forms.ValidationError(err)
        elif dataType == 'Exchange Rate Data':
            if dataItem != 'Exchange Rate':
                err = "Data item doesn't fit with the selected data type!"
                raise forms.ValidationError(err)
        else:
            if dataItem == 'Precipitation' or dataItem != 'Diesel Price' or dataItem != 'Petrol Price' or dataItem != 'Exchange Rate':
                err = "Data item doesn't fit with the selected data type!"
                raise forms.ValidationError(err)
        return cleaned_data
