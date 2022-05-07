from ..Database import databse


class Predictions:
    id = None
    location = None
    foodName = None
    percentChange = None
    firstMonth = None
    predictions = []
    curr_price = None

    def __init__(self, location, foodName, firstMonth, predictions, perChange, id=None):
        self.id = id
        self.location = location
        self.foodName = foodName
        self.percentChange = perChange
        self.firstMonth = firstMonth
        self.predictions = predictions
        self.curr_price = round(predictions[0] / perChange, 2)

    def search_food(self, foodName):
        res, err = databse.getPrediction(foodName)
        if err is not None:
            return False
        return res

    def view_predictions(self=None):
        res, err = databse.getPredictions()
        if err is not None:
            return None
        return res

    def view_recommendations(self, location):
        res, err = databse.getPredictionLocation(location)
        if err is not None:
            return False
        return res

    def predict_price(self):
        return

    def send_notification(self):
        return

    def get_locations(self):
        res, err = databse.getLocations()
        if err is not None:
            return []
        return res
