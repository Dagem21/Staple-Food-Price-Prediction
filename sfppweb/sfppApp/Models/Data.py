from ..Database import databse


class Data:

    def __init__(self, month, location, precipitation=None, maxTemp=None, minTemp=None, diesel=None, petrol=None, exrate=None, id=None):
        self.id = id
        self.month = month
        self.location = location
        self.precipitation = precipitation
        self.maxTemp = maxTemp
        self.minTemp = minTemp
        self.dieselPrice = diesel
        self.petrolPrice = petrol
        self.exRate = exrate

    def add_precipitation_data(self, value):
        if self.month is None or self.location is None or value is None:
            return False
        res, err = databse.addPrecipitationData(self.location, self.month, value)
        if err is not None:
            return False
        return True

    def add_mintemp_data(self, value):
        if self.month is None or self.location is None or value is None:
            return False
        res, err = databse.addMaxTempData(self.location, self.month, value)
        if err is not None:
            return False
        return True

    def add_maxtemp_data(self, value):
        if self.month is None or self.location is None or value is None:
            return False
        res, err = databse.addMinTempData(self.location, self.month, value)
        if err is not None:
            return False
        return True

    def add_fuel_data(self, fuel_type, value):
        if self.month is None or self.location is None or fuel_type is None or value is None:
            return False
        res, err = databse.addFuelData(self.month, self.location, fuel_type, value)
        if err is not None:
            return False
        return True

    def add_exchange_rate(self, value):
        if self.month is None or self.location is None or value is None:
            return False
        res, err = databse.addExchangeRateData(self.month, self.location, value)
        if err is not None:
            return False
        return True

    def get_data(self):
        if self.location is None:
            return []
        data, err = databse.getData(self.location)
        if err is not None:
            return []
        return data

    def get_data_month(self):
        if self.month is None or self.location is None:
            return None
        data, err = databse.getDataMonth(self.location, self.month)
        if err is not None:
            return None
        return data
