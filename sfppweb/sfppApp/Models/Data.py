from ..Database import databse


class Data:
    id = None
    month = None
    location = None
    precipitation = None
    dieselPrice = None
    petrolPrice = None
    exRate = None

    def __init__(self, month, location, precipitation=None, diesel=None, petrol=None, exrate=None, id=None):
        self.id = id
        self.month = month
        self.location = location
        self.precipitation = precipitation
        self.dieselPrice = diesel
        self.petrolPrice = petrol
        self.exRate = exrate

    def add_weather_data(self, value):
        res, err = databse.addWeatherData(self.location, self.month, value)
        if err is not None:
            return False
        return True

    def add_fuel_data(self, fuel_type, value):
        res, err = databse.addFuelData(self.month, self.location, fuel_type, value)
        if err is not None:
            return False
        return True

    def add_exchange_rate(self, value):
        res, err = databse.addExchangeRateData(self.month, self.location, value)
        if err is not None:
            return False
        return True

    def get_data(self, location):
        res, err = databse.getData(location)
        if err is not None:
            return []
        return res

    def get_data(self, location, month):
        res, err = databse.getData(location, month)
        if err is not None:
            return None
        return res
