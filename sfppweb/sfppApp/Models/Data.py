from ..Database import databse


class Data:
    id = None
    month = None
    location = None
    precipitation = None
    dieselPrice = None
    petrolPrice = None
    exRate = None

    def __init__(self, month, location, precipitation, diesel, petrol, exrate, id=None):
        self.id = id
        self.month = month
        self.location = location
        self.precipitation = precipitation
        self.dieselPrice = diesel
        self.petrolPrice = petrol
        self.exRate = exrate

    def add_weather_data(self, month, location, value):
        res, err = databse.addWeatherData(location, month, value)
        if err is not None:
            return False
        return True

    def add_fuel_data(self, month, location, fuel_type, value):
        res, err = databse.addFuelData(month, location, fuel_type, value)
        if err is not None:
            return False
        return True

    def add_exchange_rate(self, month, location, value):
        res, err = databse.addExchangeRateData(month, location, value)
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
