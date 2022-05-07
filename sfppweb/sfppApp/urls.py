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
    path('search', views.search)
]
