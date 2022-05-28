from ..Database import databse


class Notification:

    def __init__(self, location, food_name, start_month, predictions, percent_change, update_date, id=None):
        self.id = id
        self.food_name = food_name
        self.location = location
        self.start_month = start_month
        self.predictions = predictions
        self.percent_change = percent_change
        self.update_date = update_date

    def add_notification(self):
        res, err = databse.add_notification(self.food_name, self.location, self.start_month, self.predictions[0],
                                            self.predictions[1], self.predictions[3], self.predictions[3],
                                            self.predictions[4], self.predictions[5], self.percent_change)
        if err is not None:
            return False
        return True

    def send_notification(self):
        res, err = databse.send_notification(self.id)
        if err is not None:
            return False
        return True

    def get_notification(self=None, ids=None):
        res, err = databse.get_notification(ids)
        if err is not None:
            return []
        return res
