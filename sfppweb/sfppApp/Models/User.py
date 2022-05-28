import hashlib

from ..Database import databse
from ..Models.Notification import Notification


class User:

    def __init__(self, phone_number, username, password, userType, createdAt=None, uid=None, num_not=None):
        self.id = uid
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.user_type = userType
        self.created_at = createdAt
        self.num_notifications = num_not

    def hash_passowrd(self, password):
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        return hashed_password

    def login(self):
        user, err = databse.getUser(self.phone_number)
        if err is not None:
            return None, "Invalid credentials provided! Try again."
        else:
            self.password = self.hash_passowrd(self.password)
            if user.password == self.password:
                self.username = user.username
                self.user_type = user.user_type
                self.num_notifications = user.num_notifications
                return user, None
            else:
                return None, "Invalid credentials provided! Try again."

    def get_user(self):
        user, err = databse.getUser(self.phone_number)
        self.id = user.id
        self.username = user.username
        self.phone_number = user.phone_number
        self.password = user.password
        self.user_type = user.user_type
        self.num_notifications = user.num_notifications
        return

    def get_users(self):
        if self.user_type != 4:
            return [], "You are not authorized to accesses this page!"
        user, err = databse.getUsers()
        return user, err

    def signup(self):
        password = self.hash_passowrd(self.password)
        res, err = databse.addUser(self.phone_number, self.username, password, self.user_type)
        if err is not None:
            return False, err
        return True, None

    def update_account(self, password):
        self.password = self.password if password is None else self.hash_passowrd(password)
        res, err = databse.updateAccount(self.phone_number, self.password, self.user_type)
        if err is not None:
            return False
        return True

    def delete_account(self, id):
        res, err = databse.deleteAccount(id)
        if res:
            return True
        return False

    def logout(self):
        self.username = None
        self.phone_number = None
        self.password = None
        return

    def notifications(self):
        notifications, err = databse.getUserNotifications(self.id)
        if err is not None:
            return []
        notificationList = Notification.get_notification(ids=notifications)
        return notificationList

    def deleteNotification(self, notification_id):
        res, err = databse.removeNotification(self.id, notification_id)
        if err is not None:
            return False
        return True

    def registered(self):
        res, err = databse.registered(self.phone_number)
        if err is not None or not res:
            return False
        return True
