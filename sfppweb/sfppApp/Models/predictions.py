class Predictions:

    foodName = None
    percentChange = None
    predictions = {}

    def __init__(self, foodName, perChange, predictions):
        self.foodName = foodName
        self.percentChange = perChange
        self.predictions = predictions

    def search_food(self, foodName):
        return None

    def view_predictions(self):
        return None

    def view_recommendations(self, location):
        return None

    def predict_price(self):
        return

    def send_notification(self):
        return