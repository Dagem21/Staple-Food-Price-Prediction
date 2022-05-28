from django.contrib import messages
from django.shortcuts import render, redirect

from ..Forms.AddDataForm import AddDataForm
from ..Models import User, Data, Food


def addData(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
    except KeyError as e:
        pass
    finally:
        if not loggedIn:
            return redirect('/login')
        if user.user_type != 3 and user.user_type != 4:
            return redirect('/')
        form = AddDataForm(request.POST or None)
        err = None
        if request.method == 'POST' and form.is_valid():
            month = form.cleaned_data.get("month")
            location = form.cleaned_data.get("location")
            dataType = form.cleaned_data.get("dataType")
            dataItem = form.cleaned_data.get("dataItem")
            value = form.cleaned_data.get("value")

            if dataType == "Food Price":
                food = Food(dataItem, location)
                res, err = food.add_price(month, value)
                if res:
                    messages.success(request, "Data recorded!")
                else:
                    err = "Failed to record data.Try again!"
            else:
                data = Data(month, location)
                res = False
                if dataType == "Weather Data":
                    if dataItem == 'Precipitation':
                        res = data.add_precipitation_data(value)
                    elif dataItem == 'Maximum Temperature':
                        res = data.add_maxtemp_data(value)
                    elif dataItem == 'Minimum Temperature':
                        res = data.add_mintemp_data(value)
                elif dataType == "Fuel Data":
                    if dataItem == 'Diesel Price':
                        res = data.add_fuel_data('diesel_price', value)
                    elif dataItem == 'Petrol Price':
                        res = data.add_fuel_data('petrol_price', value)
                elif dataType == "Exchange Rate Data":
                    res = data.add_exchange_rate(value)
                if res:
                    messages.success(request, "Data recorded!")
                else:
                    err = "Failed to record data.Try again!"

        return render(request, 'sfppApp/addData.html', {'loggedIn': loggedIn, 'form': form, 'usertype': user.user_type,
                                                        'error': err})
