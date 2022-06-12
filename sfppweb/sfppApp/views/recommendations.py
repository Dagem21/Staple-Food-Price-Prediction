import calendar
import time
from datetime import datetime

from django.shortcuts import render, redirect

from ..Models import Predictions
from ..Models import User


def recommendations(request):
    loggedIn = False
    try:
        phone = request.session['phone']
        loggedIn = True
        user = User(phone, None, None, None)
        user.get_user()
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
        if user.user_type != 1:
            return redirect('/')
        locations = Predictions.get_locations(None)
        location = request.GET.get('location')
        if location is not None:
            chars = set(r'~!@#$%^&*()-+=`?;:\|.<>[]{}/')
            if any((c in chars) for c in location):
                err = "Unknown location. Try again with a different location!"
                return render(request, 'sfppApp/recommendations.html',
                              {'loggedIn': loggedIn,
                               'usertype': user.user_type,
                               'locations': locations,
                               'error': err})
            else:
                predictions = Predictions.view_recommendations(None, location)
                if len(predictions) == 0:
                    err = "Unknown location. Try again with a different location!"
                    return render(request, 'sfppApp/recommendations.html',
                                  {'loggedIn': loggedIn,
                                   'usertype': user.user_type,
                                   'locations': locations,
                                   'error': err})
                else:
                    first_month = predictions[0].firstMonth
                    month = get_months(first_month)
                    return render(request, 'sfppApp/recommendations.html',
                                  {'loggedIn': loggedIn,
                                   'search': True,
                                   'month': month,
                                   'predictions': predictions,
                                   'usertype': user.user_type,
                                   'locations': locations,
                                   'chosenLocation': location
                                   })
        else:
            return render(request, 'sfppApp/recommendations.html',
                          {'loggedIn': loggedIn,
                           'locations': locations,
                           'error': "Choose a location!",
                           'usertype': user.user_type})


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime(year=year, month=month, day=day)


def get_months(first_month):
    months = [first_month.strftime('%B, %Y'),
              (add_months(first_month, 1)).strftime('%B, %Y'),
              (add_months(first_month, 2)).strftime('%B, %Y'),
              (add_months(first_month, 3)).strftime('%B, %Y'),
              (add_months(first_month, 4)).strftime('%B, %Y'),
              (add_months(first_month, 5)).strftime('%B, %Y')]
    return months
