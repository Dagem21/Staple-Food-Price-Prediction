from ..Database import databse


class Weather:

    location = None
    precipitation = {}

    def __init__(self, location):
        self.location = location
        res, err = databse.getData(location)
        if err is None:
            weather = {}
            for data in res:
                weather[data.month] = data.precipitation
            self.precipitation = weather

    def set_location(self, location):
        res, err = databse.getData(location)
        if err is None:
            weather = {}
            for data in res:
                weather[data.month] = data.precipitation
            self.precipitation = weather
        else:
            return False
        self.location = location
        return True

    def get_weather(self, location):
        res, err = databse.getData(location)
        if err is None:
            weather = {}
            for data in res:
                weather[data.month] = data.precipitation
            return weather
        else:
            return None

    def get_weather(self, location, month):
        res, err = databse.getData(location)
        if err is None:
            weather = {}
            for data in res:
                weather[data.month] = data.precipitation
            return weather[month]
        else:
            return None
