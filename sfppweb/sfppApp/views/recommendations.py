from django.shortcuts import render, redirect
from dateutil.relativedelta import relativedelta
from ..Models import User
from ..Models import Predictions


def recommendations(request):
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
        if user.user_type != 1:
            return redirect('/')
        locations = Predictions.get_locations(None)
        location = request.GET.get('location')
        if location is not None:
            print(location)
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
                                   'locations': locations})
        else:
            return render(request, 'sfppApp/recommendations.html',
                          {'loggedIn': loggedIn,
                           'locations': locations,
                           'error': "Choose a location!",
                           'usertype': user.user_type})


def get_months(first_month):
    months = [first_month.strftime('%B, %Y'), (first_month + relativedelta(months=1)).strftime('%B, %Y'),
              (first_month + relativedelta(months=2)).strftime('%B, %Y'),
              (first_month + relativedelta(months=3)).strftime('%B, %Y'),
              (first_month + relativedelta(months=4)).strftime('%B, %Y'),
              (first_month + relativedelta(months=5)).strftime('%B, %Y')]
    return months
