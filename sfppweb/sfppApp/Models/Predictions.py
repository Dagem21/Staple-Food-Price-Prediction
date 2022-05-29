from ..Database import databse


class Predictions:

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

    def add_prediction(self):
        res, err = databse.addPredictions(self.foodName, self.location, self.firstMonth, self.percentChange,
                                          self.predictions[0], self.predictions[1], self.predictions[2],
                                          self.predictions[3], self.predictions[4], self.predictions[5])
        if err is not None:
            return False
        return True

    def send_notification(self):
        return

    def get_locations(self):
        res, err = databse.getLocations()
        if err is not None:
            return []
        return res
