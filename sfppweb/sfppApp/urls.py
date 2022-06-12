import time

from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('recommendations', views.recommendations),
    path('notifications', views.notifications),
    path('setting', views.setting),
    path('search', views.search),
    path('addAdmin', views.addAdmin),
    path('addData', views.addData),
    path('predict', views.predict),
    path('users', views.users),
    path('delete', views.delete),
    path('deleteNotification', views.deleteNotification)
]
