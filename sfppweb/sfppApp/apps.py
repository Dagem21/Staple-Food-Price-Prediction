import time
from threading import Thread
from django.apps import AppConfig
from .Prediction import Prediction
import datetime
import calendar


class SfppappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sfppApp'

    def ready(self):
        if not TestThread().is_alive():
            print("Thread running ...")
            # TestThread().start()


class TestThread(Thread):

    def run(self):
        while True:
            date = datetime.datetime.now()
            last_day_of_month = calendar.monthrange(date.year, date.month)[1]
            if datetime.date(date.year, date.month, date.day) == datetime.date(date.year, date.month, last_day_of_month):
                pre = Prediction.Prediction()
                pre.predictForEach()
            time.sleep(3600*24)
