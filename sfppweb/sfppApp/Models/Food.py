from ..Database import databse


class Food:

    food_name = None
    location = None
    price = None

    def __init__(self, food_name, location, price=None):
        self.food_name = food_name
        self.location = location
        if price is None:
            res, err = databse.getFoodPrice(food_name, location)
            if err is None:
                self.price = res.price
        else:
            self.price = price

    def set_location(self, location):
        self.location = location
        res, err = databse.getFoodPrice(self.food_name, location)
        if err is not None:
            return False
        self.price = res.price
        return True

    def get_price(self):
        return self.price

    def get_price(self, month):
        return self.price[month]

