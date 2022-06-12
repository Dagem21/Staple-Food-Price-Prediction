import calendar
import datetime
import time
from threading import Thread

from django.contrib import messages
from django.shortcuts import render, redirect

from ..Forms.AddDataForm import AddDataForm
from ..Models import User, Data, Food
from ..Prediction import Prediction


def addData(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        user = User(phone, None, None, None)
        user.get_user()
        loggedIn = True
        if int(time.time()) - int(request.session['time']) > 1800:
            del request.session['phone']
            del request.session['time']
            loggedIn = False
        else:
            request.session['time'] = int(time.time())
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

            if dataType == '1':
                food = Food(dataItem, location)
                res, err = food.add_price(month, value)
                if res:
                    messages.success(request, "Data recorded!")
                else:
                    err = "Failed to record data.Try again!"
            else:
                data = Data(month, location)
                res = False
                if dataType == '0':
                    if dataItem == 'Precipitation':
                        res = data.add_precipitation_data(value)
                    elif dataItem == 'Maximum Temperature':
                        res = data.add_maxtemp_data(value)
                    elif dataItem == 'Minimum Temperature':
                        res = data.add_mintemp_data(value)
                elif dataType == '2':
                    if dataItem == 'Diesel Price':
                        res = data.add_fuel_data('diesel_price', value)
                    elif dataItem == 'Petrol Price':
                        res = data.add_fuel_data('petrol_price', value)
                elif dataType == '3':
                    res = data.add_exchange_rate(value)
                if res:
                    messages.success(request, "Data recorded!")
                else:
                    err = "Failed to record data.Try again!"
        foods = ''
        foodList = AddDataForm.foodNames
        for i in foodList:
            if foods == '':
                foods = i
                continue
            foods += '|' + i
        return render(request, 'sfppApp/addData.html', {'loggedIn': loggedIn, 'form': form, 'foods': foods,
                                                        'usertype': user.user_type, 'error': err})


def predict(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        user = User(phone, None, None, None)
        user.get_user()
        loggedIn = True
        if int(time.time()) - int(request.session['time']) > 1800:
            del request.session['phone']
            del request.session['time']
            loggedIn = False
        else:
            request.session['time'] = int(time.time())
    except KeyError as e:
        pass
    finally:
        if not loggedIn:
            return redirect('/login')
        if user.user_type != 3 and user.user_type != 4:
            return redirect('/')
        TestThread().start()
        return redirect('/')


class TestThread(Thread):

    def run(self):
        pre = Prediction.Prediction()
        pre.predictForEach()
