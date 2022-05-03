class Weather:

    location = None
    precipitation = {}

    def __init__(self, location):
        self.location = location

    def set_location(self, location):
        self.location = location
        return

    def get_weather(self):
        return self

    def get_weather(self, location):
        return None

    def get_weather(self, location, month):
        return None

    def add_weather(self, location, month, precipitaiton):
        return None
