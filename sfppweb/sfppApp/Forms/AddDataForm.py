from django import forms

from ..Database import databse


class DateInput(forms.DateInput):
    input_type = 'date'


dataTypes = [
    ('Weather Data', 'Weather Data'),
    ('Food Price', 'Food Price'),
    ('Fuel Data', 'Fuel Data'),
    ('Exchange Rate Data', 'Exchange Rate Data')]
dataItems = [
    ('Precipitation', 'Precipitation'),
    ('Maximum Temperature', 'Maximum Temperature'),
    ('Minimum Temperature', 'Minimum Temperature'),
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
        widget=DateInput(
            attrs={
                'class': "form-control",
                'id': 'month',
                'data-cy': 'month'
            }
        )
    )
    location = forms.CharField(
        widget=forms.Select(
            choices=locationsList,
            attrs={
                'class': "form-control",
                'id': 'location',
                'data-cy': 'location'
            }
        ),
    )
    dataType = forms.CharField(
        widget=forms.Select(
            choices=dataTypes,
            attrs={
                'class': "form-control",
                'id': 'datatype',
                'data-cy': 'datatype'
            }
        ),
    )
    dataItem = forms.CharField(
        widget=forms.Select(
            choices=combined,
            attrs={
                'class': "form-control",
                'id': 'dataitem',
                'data-cy': 'dataitem'
            }
        ),
    )
    value = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': "form-control",
                'id': "value",
                'data-cy': 'value'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        month = cleaned_data.get("month")
        location = cleaned_data.get("location")
        dataType = cleaned_data.get("dataType")
        dataItem = cleaned_data.get("dataItem")

        chars = set(r'~!@#$%^&*()+=`?;:\|.<>[]{}/')
        if any((c in chars) for c in location):
            err = "Special characters are not allowed in this field!"
            raise forms.ValidationError({'location': err})
        else:
            if any((c in chars) for c in dataType):
                err = "Special characters are not allowed in this field!"
                raise forms.ValidationError({'dataType': err})
            else:
                if any((c in chars) for c in dataItem):
                    err = "Special characters are not allowed in this field!"
                    raise forms.ValidationError({'dataItem': err})
        if dataType == 'Weather Data':
            if dataItem != 'Precipitation' and dataItem != 'Maximum Temperature' and dataItem != 'Minimum Temperature':
                err = "Data item doesnt fit with the selected data type!"
                raise forms.ValidationError({'dataItem': err})
        elif dataType == 'Fuel Data':
            if dataItem != 'Diesel Price' and dataItem != 'Petrol Price':
                err = "Data item doesnt fit with the selected data type!"
                raise forms.ValidationError({'dataItem': err})
        elif dataType == 'Exchange Rate Data':
            if dataItem != 'Exchange Rate':
                err = "Data item doesnt fit with the selected data type!"
                raise forms.ValidationError({'dataItem': err})
        elif dataType == 'Food Price':
            if dataItem == 'Precipitation' or dataItem == 'Maximum Temperature' or dataItem == 'Minimum Temperature' \
                    or dataItem == 'Diesel Price' or dataItem == 'Petrol Price' or dataItem == 'Exchange Rate':
                err = "Data item doesnt fit with the selected data type!"
                raise forms.ValidationError({'dataItem': err})
        return cleaned_data
