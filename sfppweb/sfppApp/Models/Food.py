class Food:

    food_name = None
    location = None
    price = {}

    def __init__(self, food_name, location):
        self.food_name = food_name
        self.location = location

    def set_location(self, location):
        self.location = location
        return

    def get_price(self):
        return None

    def get_price(self, month):
        return None

