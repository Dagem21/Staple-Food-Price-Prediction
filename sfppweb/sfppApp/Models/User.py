import hashlib
from ..Database import databse


class User:
    id = None
    username = None
    password = None
    phone_number = None
    user_type = None
    created_at = None

    def __init__(self, phone_number, username, password, userType, createdAt=None, uid=None):
        self.id = uid
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.user_type = userType
        self.created_at = createdAt

    def hash_passowrd(self, password):
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        return hashed_password

    def login(self):
        user, err = databse.getUser(self.phone_number)
        if err is not None:
            return None, "Invalid credentials provided! Try again."
        else:
            if user.password == self.hash_passowrd(self.password):
                return user, None
            else:
                return None, "Invalid credentials provided! Try again."

    def get_name(self):
        return self.username

    def signup(self):
        password = self.hash_passowrd(self.password)
        res, err = databse.addUser(self.phone_number, self.username, password, self.user_type)
        if err is not None:
            return False, err
        return True, None

    def change_password(self, phone_number, password):
        res, err = databse.updatePassword(phone_number, password)
        if err is not None:
            return False
        self.password = password
        return True

    def logout(self):
        self.username = None
        self.phone_number = None
        self.password = None
        return

    def notification(self, phone_number):

        return None
